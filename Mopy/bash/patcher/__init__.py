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
#  Wrye Bash copyright (C) 2005-2009 Wrye, 2010-2020 Wrye Bash Team
#  https://github.com/wrye-bash
#
# =============================================================================
from .. import balt, bolt, bass

class PatcherInfo(object): ##: This is highly superfluous now
    __slots__ = (u'cls_vars',)

    def __init__(self, cls_vars):
        self.cls_vars = cls_vars

def exportConfig(patch_name, config, win, outDir):
    outFile = patch_name + u'_Configuration.dat'
    outDir.makedirs()
    #--File dialog
    outPath = balt.askSave(win,
        title=_(u'Export Bashed Patch configuration to:'),
        defaultDir=outDir, defaultFile=outFile,
        wildcard=u'*_Configuration.dat')
    if outPath:
        table = bolt.DataTable(bolt.PickleDict(outPath))
        table.setItem(bolt.GPath(u'Saved Bashed Patch Configuration (Python)'),
            'bash.patch.configs', config)
        table.save()

def getPatchesPath(fileName):
    """Choose the correct Bash Patches path for the file."""
    if bass.dirs[u'patches'].join(fileName).isfile():
        return bass.dirs[u'patches'].join(fileName)
    else:
        return bass.dirs[u'defaultPatches'].join(fileName)

def getPatchesList():
    """Get a basic list of potential Bash Patches."""
    return set(bass.dirs[u'patches'].list()) | set(
        bass.dirs[u'defaultPatches'].list()) # Empty list if it doesn't exist

# this is set once and stays the same for the patch execution session
_patches_set = None

def list_patches_dir():
    global _patches_set
    _patches_set = getPatchesList()

def patches_set():
    if _patches_set is None: list_patches_dir()
    return _patches_set
