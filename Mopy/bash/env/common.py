# -*- coding: utf-8 -*-
#
# GPL License and Copyright Notice ============================================
#  This file is part of Wrye Bash.
#
#  Wrye Bash is free software: you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation, either version 3
#  of the License, or (at your option) any later version.
#
#  Wrye Bash is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Wrye Bash.  If not, see <https://www.gnu.org/licenses/>.
#
#  Wrye Bash copyright (C) 2005-2009 Wrye, 2010-2021 Wrye Bash Team
#  https://github.com/wrye-bash
#
# =============================================================================
"""Common methods used by all platforms."""

import os
import stat
import sys
import warnings

from .. import bolt

def clear_read_only(filepath): # copied from bolt
    os.chmod(u'%s' % filepath, stat.S_IWUSR | stat.S_IWOTH)

# Windows store dataclasses
class WinAppVersionInfo(object):
    # PY3: Use dataclass
    def __init__(self, full_name, install_location, mutable_location, version,
                 install_time, entry_point):
        self.full_name = full_name
        self.mutable_location = mutable_location
        self.install_location = install_location
        # NOTE: the version parsed here is from the package name or app manifest
        # which do not agree in general with the canonnical "game version"
        # found in the executable.  We store it only as a fallback in case
        # the Windows Store changes (again) to where we cannot parse the EXE
        # for the real version.
        self._version = version
        self.install_time = install_time
        self.entry_point = entry_point

    def __repr__(self):
        return (u'WinAppVersionInfo(full_name=%s, install_location=%s, '
                u'mutable_location=%s, version=%s, install_time=%s, '
                u'entry_point=%s)'
                % (self.full_name, self.mutable_location, self.install_location,
                   self.version, self.install_time, self.entry_point))

class WinAppInfo(object):
    # PY3: Use a dataclass
    ## There are three names used for Windows Apps:
    ## app_name: The most human readable form
    ##   ex: `BethesdaSofworks.SkyrimSE-PC`
    ## package_name: The application name along with publisher id
    ##   ex: `BethesdaSoftworks.Skyrim_PC_3275kfvn8vcwc`
    ## full_name: The unique app name, includes version and platform
    ##   ex: `BethesdaSoftworks.TESMorrowind-PC_1.0.0.0_x86__3275kfvn8vcwc`

    def __init__(self, publisher_name=u'', publisher_id=u'', app_name=u''):
        self.publisher_name = publisher_name
        self.publisher_id = publisher_id
        self.app_name = app_name
        self.versions = dict() # full_name -> WinAppVersionInfo

    @property
    def installed(self):
        return bool(self.versions)

    def get_installed_version(self):
        """Get the most recently installed version of the app."""
        if self.installed:
            full_name = sorted(self.versions,
                key=lambda x: self.versions[x].install_time)[-1]
            return self.versions[full_name]
        else:
            return None

    def __repr__(self):
        return (u'WinAppInfo(publisher_name=%s, publisher_id=%s, app_name=%s, '
                u'versions:%i)'
                % (self.publisher_name, self.publisher_id, self.app_name,
                   len(self.versions)))

def get_game_version_fallback(test_path, ws_info):
    """A fallback method of determining the game version for Windows Store
       games.  The version returned by this method is not consistent with the
       usual executable version, so this should only be used in the even that
       a permission error prevents parsing the game file for version
       information.  This may happen at a developer's whim: Bethesda's games
       originally could not be parsed, but were later updated so they could be
       parsed."""
    warn_msg = _(u'Warning: %(game_file)s could not be parsed for version '
                 u'information.') % {'game_file': test_path}
    if ws_info.installed:
        bolt.deprint(warn_msg + u' ' +
            _(u'A fallback has been used, but may not be accurate.'))
        return ws_info.get_installed_version()._version
    else:
        bolt.deprint(warn_msg + u' ' +
            _(u'This is not a Windows Store game, your system likely needs '
              u'to be configured for file permissions.  See the Wrye Bash '
              u'General Readme for more information.'))
        return (0,0,0,0)

def get_win_store_game_paths(submod):
    """Check Windows Store-supplied game paths for the game detection
    file(s)."""
    # delayed import to pull in the right version, and avoid circular imports
    from . import get_win_store_game_info
    app_info = get_win_store_game_info(submod)
    # Select the most recently installed entry
    installed_version = app_info.get_installed_version()
    if installed_version:
        first_location = installed_version.mutable_location
        if submod.Ws.game_language_dirs:
            language_locations = [first_location.join(l)
                                  for l in submod.Ws.game_language_dirs]
            return [p for p in language_locations if p.isdir()]
        else:
            return [first_location]
    else:
        return []

def real_sys_prefix():
    if hasattr(sys, 'real_prefix'):  # running in virtualenv
        return sys.real_prefix
    elif hasattr(sys, 'base_prefix'):  # running in venv
        return sys.base_prefix
    else:
        return sys.prefix
