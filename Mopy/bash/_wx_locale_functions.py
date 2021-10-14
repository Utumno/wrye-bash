# -*- coding: utf-8 -*-
#
# This file is part of EventGhost.
# Copyright © 2005-2019 EventGhost Project <http://www.eventghost.net/>
#
# EventGhost is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 2 of the License, or (at your option)
# any later version.
#
# EventGhost is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with EventGhost. If not, see <http://www.gnu.org/licenses/>.
import ctypes
from ctypes.wintypes import DWORD, LPCWSTR, INT, BOOL, LCID, WORD

LCTYPE = DWORD
LANGID = WORD

LCID_INSTALLED = 0x00000001
LCID_SUPPORTED = 0x00000002
LOCALE_STHOUSAND = 0x0000000F
LOCALE_SMONDECIMALSEP = 0x00000016
LOCALE_SDECIMAL = 0x0000000E
LOCALE_SSHORTDATE = 0x0000001F
LOCALE_SLONGDATE = 0x00000020
LOCALE_STIMEFORMAT = 0x00001003

_kernel32 = ctypes.windll.Kernel32

# _GetLocaleInfo = _kernel32.GetLocaleInfoW
# _GetLocaleInfo.restype = INT

EnumSystemLocalesEx = _kernel32.EnumSystemLocalesEx
SetThreadLocale = _kernel32.SetThreadLocale

# Win API overrides -----------------------------------------------------------
_IsValidLocale = _kernel32.IsValidLocale
_IsValidLocale.restype = BOOL

def IsValidLocale(lcid):
    if not isinstance(lcid, LCID):
        lcid = LCID(lcid)
    if not _IsValidLocale(lcid, DWORD(LCID_SUPPORTED)):
        return False
    return bool(_IsValidLocale(lcid, DWORD(LCID_INSTALLED)))

_SetThreadUILanguage = _kernel32.SetThreadUILanguage
_SetThreadUILanguage.restype = LANGID

def SetThreadUILanguage(lcid):
    if not isinstance(lcid, LCID):
        lcid = LCID(lcid)
    _SetThreadUILanguage(lcid)

_GetThreadUILanguage = _kernel32.GetThreadUILanguage
_GetThreadUILanguage.restype = LANGID

def GetThreadUILanguage():
    lang_id = _GetThreadUILanguage()
    lcid = LCID(lang_id)
    return LCIDToLocaleName(lcid)

_LocaleNameToLCID = _kernel32.LocaleNameToLCID
_LocaleNameToLCID.restype = LCID

def LocaleNameToLCID(locale_name):
    res = _LocaleNameToLCID(
        ctypes.create_string_buffer(locale_name),
        DWORD(0)
    )
    return res or None

_LCIDToLocaleName = _kernel32.LCIDToLocaleName
_LCIDToLocaleName.restype = INT

def LCIDToLocaleName(lcid):
    if not isinstance(lcid, LCID):
        lcid = LCID(lcid)
    lpName = (ctypes.c_wchar * 0)()
    cchName = INT(0)
    dwFlags = DWORD(0)
    cchName = _LCIDToLocaleName(lcid, lpName, cchName, dwFlags)
    if not cchName:
        return
    lpName = (ctypes.c_wchar * cchName)()
    _LCIDToLocaleName(lcid, lpName, cchName, dwFlags)
    output = ''
    for i in range(cchName):
        char = lpName[i]
        if char in ('\x00', 0x0):
            break
        output += char
    return output

_GetLocaleInfoEx = _kernel32.GetLocaleInfoEx
_GetLocaleInfoEx.restype = INT

def GetLocaleInfoEx(lp_locale_name, lc_type):
    if not isinstance(lc_type, LCTYPE):
        lc_type = LCTYPE(lc_type)
    lp_lc_data = (ctypes.c_wchar * 0)()
    cch_data = _GetLocaleInfoEx(
        LPCWSTR(lp_locale_name),
        lc_type,
        lp_lc_data,
        0
    )
    if cch_data == 0:
        return ''
    lp_lc_data = (ctypes.c_wchar * cch_data)()
    res = _GetLocaleInfoEx(
        LPCWSTR(lp_locale_name),
        lc_type,
        lp_lc_data,
        cch_data
    )
    if res == 0:
        raise ctypes.WinError()
    output = ''
    for i in range(res):
        char = lp_lc_data[i]
        if char in ('\x00', 0x0):
            break
        output += char
    try:
        return int(output)
    except ValueError:
        return output

def LANGIDFROMLCID(lcid):
    return LANGID(lcid.value)
