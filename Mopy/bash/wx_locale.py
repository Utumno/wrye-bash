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

from __future__ import print_function
import wx
import sys
import ctypes
import locale as _locale
from ctypes.wintypes import WORD, LCID, DWORD, INT, WCHAR, LPCWSTR, BOOL


PY3 = sys.version_info[0] >= 3

_Locale = wx.Locale
LC_ALL = _locale.LC_ALL
LANGID = WORD
LCTYPE = DWORD

LOCALE_NAME_MAX_LENGTH = 85
LOCALE_ALLOW_NEUTRAL_NAMES = 0x08000000
LOCALE_SENGLISHLANGUAGENAME = 0x00001001
LOCALE_SENGLISHCOUNTRYNAME = 0x00001002
LOCALE_IDEFAULTANSICODEPAGE = 0x00001004
LOCALE_SNATIVELANGUAGENAME = 0x00000004
LOCALE_SLOCALIZEDLANGUAGENAME = 0x0000006f
LOCALE_SNATIVECOUNTRYNAME = 0x00000008
LOCALE_SLOCALIZEDCOUNTRYNAME = 0x00000006

LCID_INSTALLED = 0x00000001
LCID_SUPPORTED = 0x00000002

_kernel32 = ctypes.windll.Kernel32

_IsValidLocale = _kernel32.IsValidLocale
_IsValidLocale.restype = BOOL

_SetThreadUILanguage = _kernel32.SetThreadUILanguage
_SetThreadUILanguage.restype = LANGID

_GetThreadUILanguage = _kernel32.GetThreadUILanguage
_GetThreadUILanguage.restype = LANGID

_GetLocaleInfoEx = _kernel32.GetLocaleInfoEx
_GetLocaleInfoEx.restype = INT

_LocaleNameToLCID = _kernel32.LocaleNameToLCID
_LocaleNameToLCID.restype = LCID

_LCIDToLocaleName = _kernel32.LCIDToLocaleName
_LCIDToLocaleName.restype = INT

_GetLocaleInfo = _kernel32.GetLocaleInfoW
_GetLocaleInfo.restype = INT

LOCALE_STHOUSAND = 0x0000000F
LOCALE_SMONDECIMALSEP = 0x00000016
LOCALE_SDECIMAL = 0x0000000E
LOCALE_SSHORTDATE = 0x0000001F
LOCALE_SLONGDATE = 0x00000020
LOCALE_STIMEFORMAT = 0x00001003


def GetLocaleInfo(
    lpLocaleName,
    index,
    cat=wx.LOCALE_CAT_DEFAULT
):
    if index == wx.LOCALE_THOUSANDS_SEP:
        LCType = LOCALE_STHOUSAND
    elif index == wx.LOCALE_DECIMAL_POINT:
        if cat == wx.LOCALE_CAT_MONEY:
            LCType = LOCALE_SMONDECIMALSEP
        else:
            LCType = LOCALE_SDECIMAL
    elif index == wx.LOCALE_SHORT_DATE_FMT:
        LCType = LOCALE_SSHORTDATE
    elif index == wx.LOCALE_LONG_DATE_FMT:
        LCType = LOCALE_SLONGDATE
    elif index == wx.LOCALE_TIME_FMT:
        LCType = LOCALE_STIMEFORMAT
    elif index == wx.LOCALE_DATE_TIME_FMT:
        date_fmt = GetLocaleInfo(lpLocaleName, wx.LOCALE_SHORT_DATE_FMT)
        if not date_fmt:
            return ''

        time_fmt = GetLocaleInfo(lpLocaleName, wx.LOCALE_TIME_FMT)
        if not time_fmt:
            return ''

        return date_fmt + ' ' + time_fmt
    else:
        raise RuntimeError('unknown wxLocaleInfo')

    value = GetLocaleInfoEx(lpLocaleName, LCType)

    if index == wx.LOCALE_TIME_FMT:
        hour_formats = [
            '',
            '%-I',
            '%I'
        ]
        hour_count = value.count('h')
        if not hour_count:
            hour_formats = [
                '',
                '%-H',
                '%H'
            ]
            hour_count = value.count('H')

        minute_count = value.count('m')
        second_count = value.count('s')
        suffix_count = value.count('t')

        minute_formats = [
            '',
            '%-M',
            '%M'
        ]
        second_formats = [
            '',
            '%-S',
            '%S'
        ]
        suffix_formats = [
            '',
            '%p',
            '%p'
        ]

        if hour_count > 0:
            hour_format = hour_formats[hour_count]
            value = value.replace('h' * hour_count, hour_format)
            value = value.replace('H' * hour_count, hour_format)

        if minute_count > 0:
            minute_format = minute_formats[minute_count]
            value = value.replace('m' * minute_count, minute_format)

        if second_count > 0:
            second_format = second_formats[second_count]
            value = value.replace('s' * second_count, second_format)

        if suffix_count > 0:
            suffix_format = suffix_formats[suffix_count]
            value = value.replace('t' * suffix_count, suffix_format)

    elif index in (wx.LOCALE_SHORT_DATE_FMT, wx.LOCALE_LONG_DATE_FMT):
        items = value.split(' ')
        for i, item in enumerate(items):
            month_count = item.count('M')
            day_count = item.count('d')
            year_count = item.count('y')

            month_formats = [
                '',
                '%-m',
                '%m',
                '%b',
                '%B'
            ]
            day_formats = [
                '',
                '%-d',
                '%d',
                '%a',
                '%A'
            ]
            year_formats = [
                '',
                '%y',
                '%y',
                '',
                '%Y',
                '%Y'
            ]

            if month_count > 0:
                month_format = month_formats[month_count]
                item = item.replace('M' * month_count, month_format)

            if day_count > 0:
                day_format = day_formats[day_count]
                item = item.replace('d' * day_count, day_format)

            if year_count > 0:
                year_format = year_formats[year_count]
                item = item.replace('y' * year_count, year_format)

            items[i] = item

        value = ' '.join(items)

    return value


def SetThreadUILanguage(lcid):
    if not isinstance(lcid, LCID):
        lcid = LCID(lcid)

    _SetThreadUILanguage(lcid)


def IsValidLocale(lcid):
    if not isinstance(lcid, LCID):
        lcid = LCID(lcid)

    if not _IsValidLocale(lcid, DWORD(LCID_SUPPORTED)):
        return False

    return bool(_IsValidLocale(lcid, DWORD(LCID_INSTALLED)))


def GetThreadUILanguage():
    lang_id = _GetThreadUILanguage()
    lcid = LCIDFROMLANGID(lang_id)
    return LCIDToLocaleName(lcid)


def LocaleNameToLCID(locale_name):
    if isinstance(locale_name, str):
        if PY3:
            pass
            # locale_name = locale_name.encode('utf-8')
        else:
            # noinspection PyUnresolvedReferences
            locale_name = unicode(locale_name)

    res = _LocaleNameToLCID(
        ctypes.create_string_buffer(locale_name),
        DWORD(0)
    )
    if res == 0:
        return None
    return res


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


def LCIDFROMLANGID(lang_id):
    return LCID(lang_id)


def LANGIDFROMLCID(lcid):
    return LANGID(lcid.value)


def SETWINLANG(info, lang, sublang):
    info.WinLang = lang,
    info.WinSublang = sublang



def LNG(wxlang, canonical, winlang, winsublang, layout, desc):
    info = LanguageInfo()
    info.Language = wxlang
    info.CanonicalName = canonical
    info.LayoutDirection = layout
    info.Description = desc
    SETWINLANG(info, winlang, winsublang)
    Locale.AddLanguage(info)
    return info

def _add_languages_to_db():
    LNG(wx.LANGUAGE_ABKHAZIAN, "ab", 0, 0, wx.Layout_LeftToRight, "Abkhazian")
    LNG(wx.LANGUAGE_AFAR, "aa", 0, 0, wx.Layout_LeftToRight, "Afar")
    LNG(wx.LANGUAGE_AFRIKAANS, "af", LANG_AFRIKAANS, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Afrikaans")
    LNG(wx.LANGUAGE_ALBANIAN, "sq_AL", LANG_ALBANIAN, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Albanian")
    LNG(wx.LANGUAGE_AMHARIC, "am", 0, 0, wx.Layout_LeftToRight, "Amharic")
    LNG(wx.LANGUAGE_ARABIC, "ar", LANG_ARABIC, SUBLANG_DEFAULT, wx.Layout_RightToLeft, "Arabic")
    LNG(wx.LANGUAGE_ARABIC_ALGERIA, "ar_DZ", LANG_ARABIC, SUBLANG_ARABIC_ALGERIA, wx.Layout_RightToLeft,
        "Arabic (Algeria)")
    LNG(wx.LANGUAGE_ARABIC_BAHRAIN, "ar_BH", LANG_ARABIC, SUBLANG_ARABIC_BAHRAIN, wx.Layout_RightToLeft,
        "Arabic (Bahrain)")
    LNG(wx.LANGUAGE_ARABIC_EGYPT, "ar_EG", LANG_ARABIC, SUBLANG_ARABIC_EGYPT, wx.Layout_RightToLeft, "Arabic (Egypt)")
    LNG(wx.LANGUAGE_ARABIC_IRAQ, "ar_IQ", LANG_ARABIC, SUBLANG_ARABIC_IRAQ, wx.Layout_RightToLeft, "Arabic (Iraq)")
    LNG(wx.LANGUAGE_ARABIC_JORDAN, "ar_JO", LANG_ARABIC, SUBLANG_ARABIC_JORDAN, wx.Layout_RightToLeft,
        "Arabic (Jordan)")
    LNG(wx.LANGUAGE_ARABIC_KUWAIT, "ar_KW", LANG_ARABIC, SUBLANG_ARABIC_KUWAIT, wx.Layout_RightToLeft,
        "Arabic (Kuwait)")
    LNG(wx.LANGUAGE_ARABIC_LEBANON, "ar_LB", LANG_ARABIC, SUBLANG_ARABIC_LEBANON, wx.Layout_RightToLeft,
        "Arabic (Lebanon)")
    LNG(wx.LANGUAGE_ARABIC_LIBYA, "ar_LY", LANG_ARABIC, SUBLANG_ARABIC_LIBYA, wx.Layout_RightToLeft, "Arabic (Libya)")
    LNG(wx.LANGUAGE_ARABIC_MOROCCO, "ar_MA", LANG_ARABIC, SUBLANG_ARABIC_MOROCCO, wx.Layout_RightToLeft,
        "Arabic (Morocco)")
    LNG(wx.LANGUAGE_ARABIC_OMAN, "ar_OM", LANG_ARABIC, SUBLANG_ARABIC_OMAN, wx.Layout_RightToLeft, "Arabic (Oman)")
    LNG(wx.LANGUAGE_ARABIC_QATAR, "ar_QA", LANG_ARABIC, SUBLANG_ARABIC_QATAR, wx.Layout_RightToLeft, "Arabic (Qatar)")
    LNG(wx.LANGUAGE_ARABIC_SAUDI_ARABIA, "ar_SA", LANG_ARABIC, SUBLANG_ARABIC_SAUDI_ARABIA, wx.Layout_RightToLeft,
        "Arabic (Saudi Arabia)")
    LNG(wx.LANGUAGE_ARABIC_SUDAN, "ar_SD", 0, 0, wx.Layout_RightToLeft, "Arabic (Sudan)")
    LNG(wx.LANGUAGE_ARABIC_SYRIA, "ar_SY", LANG_ARABIC, SUBLANG_ARABIC_SYRIA, wx.Layout_RightToLeft, "Arabic (Syria)")
    LNG(wx.LANGUAGE_ARABIC_TUNISIA, "ar_TN", LANG_ARABIC, SUBLANG_ARABIC_TUNISIA, wx.Layout_RightToLeft,
        "Arabic (Tunisia)")
    LNG(wx.LANGUAGE_ARABIC_UAE, "ar_AE", LANG_ARABIC, SUBLANG_ARABIC_UAE, wx.Layout_RightToLeft, "Arabic (Uae)")
    LNG(wx.LANGUAGE_ARABIC_YEMEN, "ar_YE", LANG_ARABIC, SUBLANG_ARABIC_YEMEN, wx.Layout_RightToLeft, "Arabic (Yemen)")
    LNG(wx.LANGUAGE_ARMENIAN, "hy", LANG_ARMENIAN, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Armenian")
    LNG(wx.LANGUAGE_ASSAMESE, "as", LANG_ASSAMESE, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Assamese")
    LNG(wx.LANGUAGE_ASTURIAN, "ast", 0, 0, wx.Layout_LeftToRight, "Asturian")
    LNG(wx.LANGUAGE_AYMARA, "ay", 0, 0, wx.Layout_LeftToRight, "Aymara")
    LNG(wx.LANGUAGE_AZERI, "az", LANG_AZERI, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Azeri")
    LNG(wx.LANGUAGE_AZERI_CYRILLIC, "az", LANG_AZERI, SUBLANG_AZERI_CYRILLIC, wx.Layout_LeftToRight, "Azeri (Cyrillic)")
    LNG(wx.LANGUAGE_AZERI_LATIN, "az", LANG_AZERI, SUBLANG_AZERI_LATIN, wx.Layout_LeftToRight, "Azeri (Latin)")
    LNG(wx.LANGUAGE_BASHKIR, "ba", 0, 0, wx.Layout_LeftToRight, "Bashkir")
    LNG(wx.LANGUAGE_BASQUE, "eu_ES", LANG_BASQUE, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Basque")
    LNG(wx.LANGUAGE_BELARUSIAN, "be_BY", LANG_BELARUSIAN, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Belarusian")
    LNG(wx.LANGUAGE_BENGALI, "bn", LANG_BENGALI, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Bengali")
    LNG(wx.LANGUAGE_BHUTANI, "dz", 0, 0, wx.Layout_LeftToRight, "Bhutani")
    LNG(wx.LANGUAGE_BIHARI, "bh", 0, 0, wx.Layout_LeftToRight, "Bihari")
    LNG(wx.LANGUAGE_BISLAMA, "bi", 0, 0, wx.Layout_LeftToRight, "Bislama")
    LNG(wx.LANGUAGE_BOSNIAN, "bs", LANG_BOSNIAN, SUBLANG_BOSNIAN_BOSNIA_HERZEGOVINA_LATIN, wx.Layout_LeftToRight,
        "Bosnian")
    LNG(wx.LANGUAGE_BRETON, "br", 0, 0, wx.Layout_LeftToRight, "Breton")
    LNG(wx.LANGUAGE_BULGARIAN, "bg_BG", LANG_BULGARIAN, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Bulgarian")
    LNG(wx.LANGUAGE_BURMESE, "my", 0, 0, wx.Layout_LeftToRight, "Burmese")
    LNG(wx.LANGUAGE_CATALAN, "ca_ES", LANG_CATALAN, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Catalan")
    LNG(wx.LANGUAGE_CHINESE, "zh_TW", LANG_CHINESE, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Chinese")
    LNG(wx.LANGUAGE_CHINESE_SIMPLIFIED, "zh_CN", LANG_CHINESE, SUBLANG_CHINESE_SIMPLIFIED, wx.Layout_LeftToRight,
        "Chinese (Simplified)")
    LNG(wx.LANGUAGE_CHINESE_TRADITIONAL, "zh_TW", LANG_CHINESE, SUBLANG_CHINESE_TRADITIONAL, wx.Layout_LeftToRight,
        "Chinese (Traditional)")
    LNG(wx.LANGUAGE_CHINESE_HONGKONG, "zh_HK", LANG_CHINESE, SUBLANG_CHINESE_HONGKONG, wx.Layout_LeftToRight,
        "Chinese (Hongkong)")
    LNG(wx.LANGUAGE_CHINESE_MACAU, "zh_MO", LANG_CHINESE, SUBLANG_CHINESE_MACAU, wx.Layout_LeftToRight,
        "Chinese (Macau)")
    LNG(wx.LANGUAGE_CHINESE_SINGAPORE, "zh_SG", LANG_CHINESE, SUBLANG_CHINESE_SINGAPORE, wx.Layout_LeftToRight,
        "Chinese (Singapore)")
    LNG(wx.LANGUAGE_CHINESE_TAIWAN, "zh_TW", LANG_CHINESE, SUBLANG_CHINESE_TRADITIONAL, wx.Layout_LeftToRight,
        "Chinese (Taiwan)")
    LNG(wx.LANGUAGE_CORSICAN, "co", 0, 0, wx.Layout_LeftToRight, "Corsican")
    LNG(wx.LANGUAGE_CROATIAN, "hr_HR", LANG_CROATIAN, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Croatian")
    LNG(wx.LANGUAGE_CZECH, "cs_CZ", LANG_CZECH, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Czech")
    LNG(wx.LANGUAGE_DANISH, "da_DK", LANG_DANISH, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Danish")
    LNG(wx.LANGUAGE_DUTCH, "nl_NL", LANG_DUTCH, SUBLANG_DUTCH, wx.Layout_LeftToRight, "Dutch")
    LNG(wx.LANGUAGE_DUTCH_BELGIAN, "nl_BE", LANG_DUTCH, SUBLANG_DUTCH_BELGIAN, wx.Layout_LeftToRight, "Dutch (Belgian)")
    LNG(wx.LANGUAGE_ENGLISH, "en_GB", LANG_ENGLISH, SUBLANG_ENGLISH_UK, wx.Layout_LeftToRight, "English")
    LNG(wx.LANGUAGE_ENGLISH_UK, "en_GB", LANG_ENGLISH, SUBLANG_ENGLISH_UK, wx.Layout_LeftToRight, "English (U.K.)")
    LNG(wx.LANGUAGE_ENGLISH_US, "en_US", LANG_ENGLISH, SUBLANG_ENGLISH_US, wx.Layout_LeftToRight, "English (U.S.)")
    LNG(wx.LANGUAGE_ENGLISH_AUSTRALIA, "en_AU", LANG_ENGLISH, SUBLANG_ENGLISH_AUS, wx.Layout_LeftToRight,
        "English (Australia)")
    LNG(wx.LANGUAGE_ENGLISH_BELIZE, "en_BZ", LANG_ENGLISH, SUBLANG_ENGLISH_BELIZE, wx.Layout_LeftToRight,
        "English (Belize)")
    LNG(wx.LANGUAGE_ENGLISH_BOTSWANA, "en_BW", 0, 0, wx.Layout_LeftToRight, "English (Botswana)")
    LNG(wx.LANGUAGE_ENGLISH_CANADA, "en_CA", LANG_ENGLISH, SUBLANG_ENGLISH_CAN, wx.Layout_LeftToRight,
        "English (Canada)")
    LNG(wx.LANGUAGE_ENGLISH_CARIBBEAN, "en_CB", LANG_ENGLISH, SUBLANG_ENGLISH_CARIBBEAN, wx.Layout_LeftToRight,
        "English (Caribbean)")
    LNG(wx.LANGUAGE_ENGLISH_DENMARK, "en_DK", 0, 0, wx.Layout_LeftToRight, "English (Denmark)")
    LNG(wx.LANGUAGE_ENGLISH_EIRE, "en_IE", LANG_ENGLISH, SUBLANG_ENGLISH_EIRE, wx.Layout_LeftToRight, "English (Eire)")
    LNG(wx.LANGUAGE_ENGLISH_JAMAICA, "en_JM", LANG_ENGLISH, SUBLANG_ENGLISH_JAMAICA, wx.Layout_LeftToRight,
        "English (Jamaica)")
    LNG(wx.LANGUAGE_ENGLISH_NEW_ZEALAND, "en_NZ", LANG_ENGLISH, SUBLANG_ENGLISH_NZ, wx.Layout_LeftToRight,
        "English (New Zealand)")
    LNG(wx.LANGUAGE_ENGLISH_PHILIPPINES, "en_PH", LANG_ENGLISH, SUBLANG_ENGLISH_PHILIPPINES, wx.Layout_LeftToRight,
        "English (Philippines)")
    LNG(wx.LANGUAGE_ENGLISH_SOUTH_AFRICA, "en_ZA", LANG_ENGLISH, SUBLANG_ENGLISH_SOUTH_AFRICA, wx.Layout_LeftToRight,
        "English (South Africa)")
    LNG(wx.LANGUAGE_ENGLISH_TRINIDAD, "en_TT", LANG_ENGLISH, SUBLANG_ENGLISH_TRINIDAD, wx.Layout_LeftToRight,
        "English (Trinidad)")
    LNG(wx.LANGUAGE_ENGLISH_ZIMBABWE, "en_ZW", LANG_ENGLISH, SUBLANG_ENGLISH_ZIMBABWE, wx.Layout_LeftToRight,
        "English (Zimbabwe)")
    LNG(wx.LANGUAGE_ESPERANTO, "eo", 0, 0, wx.Layout_LeftToRight, "Esperanto")
    LNG(wx.LANGUAGE_ESTONIAN, "et_EE", LANG_ESTONIAN, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Estonian")
    LNG(wx.LANGUAGE_FAEROESE, "fo_FO", LANG_FAEROESE, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Faeroese")
    LNG(wx.LANGUAGE_FARSI, "fa_IR", LANG_FARSI, SUBLANG_DEFAULT, wx.Layout_RightToLeft, "Farsi")
    LNG(wx.LANGUAGE_FIJI, "fj", 0, 0, wx.Layout_LeftToRight, "Fiji")
    LNG(wx.LANGUAGE_FINNISH, "fi_FI", LANG_FINNISH, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Finnish")
    LNG(wx.LANGUAGE_FRENCH, "fr_FR", LANG_FRENCH, SUBLANG_FRENCH, wx.Layout_LeftToRight, "French")
    LNG(wx.LANGUAGE_FRENCH_BELGIAN, "fr_BE", LANG_FRENCH, SUBLANG_FRENCH_BELGIAN, wx.Layout_LeftToRight,
        "French (Belgian)")
    LNG(wx.LANGUAGE_FRENCH_CANADIAN, "fr_CA", LANG_FRENCH, SUBLANG_FRENCH_CANADIAN, wx.Layout_LeftToRight,
        "French (Canadian)")
    LNG(wx.LANGUAGE_FRENCH_LUXEMBOURG, "fr_LU", LANG_FRENCH, SUBLANG_FRENCH_LUXEMBOURG, wx.Layout_LeftToRight,
        "French (Luxembourg)")
    LNG(wx.LANGUAGE_FRENCH_MONACO, "fr_MC", LANG_FRENCH, SUBLANG_FRENCH_MONACO, wx.Layout_LeftToRight,
        "French (Monaco)")
    LNG(wx.LANGUAGE_FRENCH_SWISS, "fr_CH", LANG_FRENCH, SUBLANG_FRENCH_SWISS, wx.Layout_LeftToRight, "French (Swiss)")
    LNG(wx.LANGUAGE_FRISIAN, "fy", LANG_FRISIAN, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Frisian")
    LNG(wx.LANGUAGE_GALICIAN, "gl_ES", 0, 0, wx.Layout_LeftToRight, "Galician")
    LNG(wx.LANGUAGE_GEORGIAN, "ka_GE", LANG_GEORGIAN, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Georgian")
    LNG(wx.LANGUAGE_GERMAN, "de_DE", LANG_GERMAN, SUBLANG_GERMAN, wx.Layout_LeftToRight, "German")
    LNG(wx.LANGUAGE_GERMAN_AUSTRIAN, "de_AT", LANG_GERMAN, SUBLANG_GERMAN_AUSTRIAN, wx.Layout_LeftToRight,
        "German (Austrian)")
    LNG(wx.LANGUAGE_GERMAN_BELGIUM, "de_BE", 0, 0, wx.Layout_LeftToRight, "German (Belgium)")
    LNG(wx.LANGUAGE_GERMAN_LIECHTENSTEIN, "de_LI", LANG_GERMAN, SUBLANG_GERMAN_LIECHTENSTEIN, wx.Layout_LeftToRight,
        "German (Liechtenstein)")
    LNG(wx.LANGUAGE_GERMAN_LUXEMBOURG, "de_LU", LANG_GERMAN, SUBLANG_GERMAN_LUXEMBOURG, wx.Layout_LeftToRight,
        "German (Luxembourg)")
    LNG(wx.LANGUAGE_GERMAN_SWISS, "de_CH", LANG_GERMAN, SUBLANG_GERMAN_SWISS, wx.Layout_LeftToRight, "German (Swiss)")
    LNG(wx.LANGUAGE_GREEK, "el_GR", LANG_GREEK, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Greek")
    LNG(wx.LANGUAGE_GREENLANDIC, "kl_GL", 0, 0, wx.Layout_LeftToRight, "Greenlandic")
    LNG(wx.LANGUAGE_GUARANI, "gn", 0, 0, wx.Layout_LeftToRight, "Guarani")
    LNG(wx.LANGUAGE_GUJARATI, "gu", LANG_GUJARATI, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Gujarati")
    LNG(wx.LANGUAGE_HAUSA, "ha", 0, 0, wx.Layout_LeftToRight, "Hausa")
    LNG(wx.LANGUAGE_HEBREW, "he_IL", LANG_HEBREW, SUBLANG_DEFAULT, wx.Layout_RightToLeft, "Hebrew")
    LNG(wx.LANGUAGE_HINDI, "hi_IN", LANG_HINDI, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Hindi")
    LNG(wx.LANGUAGE_HUNGARIAN, "hu_HU", LANG_HUNGARIAN, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Hungarian")
    LNG(wx.LANGUAGE_ICELANDIC, "is_IS", LANG_ICELANDIC, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Icelandic")
    LNG(wx.LANGUAGE_INDONESIAN, "id_ID", LANG_INDONESIAN, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Indonesian")
    LNG(wx.LANGUAGE_INTERLINGUA, "ia", 0, 0, wx.Layout_LeftToRight, "Interlingua")
    LNG(wx.LANGUAGE_INTERLINGUE, "ie", 0, 0, wx.Layout_LeftToRight, "Interlingue")
    LNG(wx.LANGUAGE_INUKTITUT, "iu", 0, 0, wx.Layout_LeftToRight, "Inuktitut")
    LNG(wx.LANGUAGE_INUPIAK, "ik", 0, 0, wx.Layout_LeftToRight, "Inupiak")
    LNG(wx.LANGUAGE_IRISH, "ga_IE", 0, 0, wx.Layout_LeftToRight, "Irish")
    LNG(wx.LANGUAGE_ITALIAN, "it_IT", LANG_ITALIAN, SUBLANG_ITALIAN, wx.Layout_LeftToRight, "Italian")
    LNG(wx.LANGUAGE_ITALIAN_SWISS, "it_CH", LANG_ITALIAN, SUBLANG_ITALIAN_SWISS, wx.Layout_LeftToRight,
        "Italian (Swiss)")
    LNG(wx.LANGUAGE_JAPANESE, "ja_JP", LANG_JAPANESE, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Japanese")
    LNG(wx.LANGUAGE_JAVANESE, "jv", 0, 0, wx.Layout_LeftToRight, "Javanese")
    LNG(wx.LANGUAGE_KABYLE, "kab", LANG_KABYLE, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Kabyle")
    LNG(wx.LANGUAGE_KANNADA, "kn", LANG_KANNADA, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Kannada")
    LNG(wx.LANGUAGE_KASHMIRI, "ks", LANG_KASHMIRI, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Kashmiri")
    LNG(wx.LANGUAGE_KASHMIRI_INDIA, "ks_IN", LANG_KASHMIRI, SUBLANG_KASHMIRI_INDIA, wx.Layout_LeftToRight,
        "Kashmiri (India)")
    LNG(wx.LANGUAGE_KAZAKH, "kk", LANG_KAZAK, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Kazakh")
    LNG(wx.LANGUAGE_KERNEWEK, "kw_GB", 0, 0, wx.Layout_LeftToRight, "Kernewek")
    # LNG(wx.LANGUAGE_KHMER, "km", 0, 0, wx.Layout_LeftToRight, "Khmer")
    LNG(wx.LANGUAGE_KINYARWANDA, "rw", 0, 0, wx.Layout_LeftToRight, "Kinyarwanda")
    LNG(wx.LANGUAGE_KIRGHIZ, "ky", 0, 0, wx.Layout_LeftToRight, "Kirghiz")
    LNG(wx.LANGUAGE_KIRUNDI, "rn", 0, 0, wx.Layout_LeftToRight, "Kirundi")
    LNG(wx.LANGUAGE_KONKANI, "", LANG_KONKANI, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Konkani")
    LNG(wx.LANGUAGE_KOREAN, "ko_KR", LANG_KOREAN, SUBLANG_KOREAN, wx.Layout_LeftToRight, "Korean")
    LNG(wx.LANGUAGE_KURDISH, "ku_TR", 0, 0, wx.Layout_LeftToRight, "Kurdish")
    LNG(wx.LANGUAGE_LAOTHIAN, "lo", 0, 0, wx.Layout_LeftToRight, "Laothian")
    LNG(wx.LANGUAGE_LATIN, "la", 0, 0, wx.Layout_LeftToRight, "Latin")
    LNG(wx.LANGUAGE_LATVIAN, "lv_LV", LANG_LATVIAN, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Latvian")
    LNG(wx.LANGUAGE_LINGALA, "ln", 0, 0, wx.Layout_LeftToRight, "Lingala")
    LNG(wx.LANGUAGE_LITHUANIAN, "lt_LT", LANG_LITHUANIAN, SUBLANG_LITHUANIAN, wx.Layout_LeftToRight, "Lithuanian")
    LNG(wx.LANGUAGE_MACEDONIAN, "mk_MK", LANG_MACEDONIAN, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Macedonian")
    LNG(wx.LANGUAGE_MALAGASY, "mg", 0, 0, wx.Layout_LeftToRight, "Malagasy")
    LNG(wx.LANGUAGE_MALAY, "ms_MY", LANG_MALAY, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Malay")
    LNG(wx.LANGUAGE_MALAYALAM, "ml", LANG_MALAYALAM, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Malayalam")
    LNG(wx.LANGUAGE_MALAY_BRUNEI_DARUSSALAM, "ms_BN", LANG_MALAY, SUBLANG_MALAY_BRUNEI_DARUSSALAM,
        wx.Layout_LeftToRight, "Malay (Brunei Darussalam)")
    LNG(wx.LANGUAGE_MALAY_MALAYSIA, "ms_MY", LANG_MALAY, SUBLANG_MALAY_MALAYSIA, wx.Layout_LeftToRight,
        "Malay (Malaysia)")
    LNG(wx.LANGUAGE_MALTESE, "mt_MT", 0, 0, wx.Layout_LeftToRight, "Maltese")
    LNG(wx.LANGUAGE_MANIPURI, "", LANG_MANIPURI, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Manipuri")
    LNG(wx.LANGUAGE_MAORI, "mi", 0, 0, wx.Layout_LeftToRight, "Maori")
    LNG(wx.LANGUAGE_MARATHI, "mr_IN", LANG_MARATHI, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Marathi")
    LNG(wx.LANGUAGE_MOLDAVIAN, "mo", 0, 0, wx.Layout_LeftToRight, "Moldavian")
    LNG(wx.LANGUAGE_MONGOLIAN, "mn", 0, 0, wx.Layout_LeftToRight, "Mongolian")
    LNG(wx.LANGUAGE_NAURU, "na", 0, 0, wx.Layout_LeftToRight, "Nauru")
    LNG(wx.LANGUAGE_NEPALI, "ne_NP", LANG_NEPALI, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Nepali")
    LNG(wx.LANGUAGE_NEPALI_INDIA, "ne_IN", LANG_NEPALI, SUBLANG_NEPALI_INDIA, wx.Layout_LeftToRight, "Nepali (India)")
    LNG(wx.LANGUAGE_NORWEGIAN_BOKMAL, "nb_NO", LANG_NORWEGIAN, SUBLANG_NORWEGIAN_BOKMAL, wx.Layout_LeftToRight,
        "Norwegian (Bokmal)")
    LNG(wx.LANGUAGE_NORWEGIAN_NYNORSK, "nn_NO", LANG_NORWEGIAN, SUBLANG_NORWEGIAN_NYNORSK, wx.Layout_LeftToRight,
        "Norwegian (Nynorsk)")
    LNG(wx.LANGUAGE_OCCITAN, "oc", 0, 0, wx.Layout_LeftToRight, "Occitan")
    LNG(wx.LANGUAGE_ORIYA, "or", LANG_ORIYA, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Oriya")
    LNG(wx.LANGUAGE_OROMO, "om", 0, 0, wx.Layout_LeftToRight, "(Afan) Oromo")
    LNG(wx.LANGUAGE_PASHTO, "ps", 0, 0, wx.Layout_LeftToRight, "Pashto, Pushto")
    LNG(wx.LANGUAGE_POLISH, "pl_PL", LANG_POLISH, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Polish")
    LNG(wx.LANGUAGE_PORTUGUESE, "pt_PT", LANG_PORTUGUESE, SUBLANG_PORTUGUESE, wx.Layout_LeftToRight, "Portuguese")
    LNG(wx.LANGUAGE_PORTUGUESE_BRAZILIAN, "pt_BR", LANG_PORTUGUESE, SUBLANG_PORTUGUESE_BRAZILIAN, wx.Layout_LeftToRight,
        "Portuguese (Brazilian)")
    LNG(wx.LANGUAGE_PUNJABI, "pa", LANG_PUNJABI, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Punjabi")
    LNG(wx.LANGUAGE_QUECHUA, "qu", 0, 0, wx.Layout_LeftToRight, "Quechua")
    LNG(wx.LANGUAGE_RHAETO_ROMANCE, "rm", 0, 0, wx.Layout_LeftToRight, "Rhaeto-Romance")
    LNG(wx.LANGUAGE_ROMANIAN, "ro_RO", LANG_ROMANIAN, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Romanian")
    LNG(wx.LANGUAGE_RUSSIAN, "ru_RU", LANG_RUSSIAN, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Russian")
    LNG(wx.LANGUAGE_RUSSIAN_UKRAINE, "ru_UA", 0, 0, wx.Layout_LeftToRight, "Russian (Ukraine)")
    LNG(wx.LANGUAGE_SAMI, "se_NO", LANG_SAMI, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Northern Sami")
    LNG(wx.LANGUAGE_SAMOAN, "sm", 0, 0, wx.Layout_LeftToRight, "Samoan")
    LNG(wx.LANGUAGE_SANGHO, "sg", 0, 0, wx.Layout_LeftToRight, "Sangho")
    LNG(wx.LANGUAGE_SANSKRIT, "sa", LANG_SANSKRIT, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Sanskrit")
    LNG(wx.LANGUAGE_SCOTS_GAELIC, "gd", 0, 0, wx.Layout_LeftToRight, "Scots Gaelic")
    LNG(wx.LANGUAGE_SERBIAN, "sr_RS", LANG_SERBIAN, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Serbian")
    LNG(wx.LANGUAGE_SERBIAN_CYRILLIC, "sr_RS", LANG_SERBIAN, SUBLANG_SERBIAN_CYRILLIC, wx.Layout_LeftToRight,
        "Serbian (Cyrillic)")
    LNG(wx.LANGUAGE_SERBIAN_LATIN, "sr_RS@latin", LANG_SERBIAN, SUBLANG_SERBIAN_LATIN, wx.Layout_LeftToRight,
        "Serbian (Latin)")
    LNG(wx.LANGUAGE_SERBIAN_CYRILLIC, "sr_YU", LANG_SERBIAN, SUBLANG_SERBIAN_CYRILLIC, wx.Layout_LeftToRight,
        "Serbian (Cyrillic)")
    LNG(wx.LANGUAGE_SERBIAN_LATIN, "sr_YU@latin", LANG_SERBIAN, SUBLANG_SERBIAN_LATIN, wx.Layout_LeftToRight,
        "Serbian (Latin)")
    LNG(wx.LANGUAGE_SERBO_CROATIAN, "sh", 0, 0, wx.Layout_LeftToRight, "Serbo-Croatian")
    LNG(wx.LANGUAGE_SESOTHO, "st", 0, 0, wx.Layout_LeftToRight, "Sesotho")
    LNG(wx.LANGUAGE_SETSWANA, "tn", 0, 0, wx.Layout_LeftToRight, "Setswana")
    LNG(wx.LANGUAGE_SHONA, "sn", 0, 0, wx.Layout_LeftToRight, "Shona")
    LNG(wx.LANGUAGE_SINDHI, "sd", LANG_SINDHI, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Sindhi")
    LNG(wx.LANGUAGE_SINHALESE, "si", 0, 0, wx.Layout_LeftToRight, "Sinhalese")
    LNG(wx.LANGUAGE_SISWATI, "ss", 0, 0, wx.Layout_LeftToRight, "Siswati")
    LNG(wx.LANGUAGE_SLOVAK, "sk_SK", LANG_SLOVAK, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Slovak")
    LNG(wx.LANGUAGE_SLOVENIAN, "sl_SI", LANG_SLOVENIAN, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Slovenian")
    LNG(wx.LANGUAGE_SOMALI, "so", 0, 0, wx.Layout_LeftToRight, "Somali")
    LNG(wx.LANGUAGE_SPANISH, "es_ES", LANG_SPANISH, SUBLANG_SPANISH, wx.Layout_LeftToRight, "Spanish")
    LNG(wx.LANGUAGE_SPANISH_ARGENTINA, "es_AR", LANG_SPANISH, SUBLANG_SPANISH_ARGENTINA, wx.Layout_LeftToRight,
        "Spanish (Argentina)")
    LNG(wx.LANGUAGE_SPANISH_BOLIVIA, "es_BO", LANG_SPANISH, SUBLANG_SPANISH_BOLIVIA, wx.Layout_LeftToRight,
        "Spanish (Bolivia)")
    LNG(wx.LANGUAGE_SPANISH_CHILE, "es_CL", LANG_SPANISH, SUBLANG_SPANISH_CHILE, wx.Layout_LeftToRight,
        "Spanish (Chile)")
    LNG(wx.LANGUAGE_SPANISH_COLOMBIA, "es_CO", LANG_SPANISH, SUBLANG_SPANISH_COLOMBIA, wx.Layout_LeftToRight,
        "Spanish (Colombia)")
    LNG(wx.LANGUAGE_SPANISH_COSTA_RICA, "es_CR", LANG_SPANISH, SUBLANG_SPANISH_COSTA_RICA, wx.Layout_LeftToRight,
        "Spanish (Costa Rica)")
    LNG(wx.LANGUAGE_SPANISH_DOMINICAN_REPUBLIC, "es_DO", LANG_SPANISH, SUBLANG_SPANISH_DOMINICAN_REPUBLIC,
        wx.Layout_LeftToRight, "Spanish (Dominican republic)")
    LNG(wx.LANGUAGE_SPANISH_ECUADOR, "es_EC", LANG_SPANISH, SUBLANG_SPANISH_ECUADOR, wx.Layout_LeftToRight,
        "Spanish (Ecuador)")
    LNG(wx.LANGUAGE_SPANISH_EL_SALVADOR, "es_SV", LANG_SPANISH, SUBLANG_SPANISH_EL_SALVADOR, wx.Layout_LeftToRight,
        "Spanish (El Salvador)")
    LNG(wx.LANGUAGE_SPANISH_GUATEMALA, "es_GT", LANG_SPANISH, SUBLANG_SPANISH_GUATEMALA, wx.Layout_LeftToRight,
        "Spanish (Guatemala)")
    LNG(wx.LANGUAGE_SPANISH_HONDURAS, "es_HN", LANG_SPANISH, SUBLANG_SPANISH_HONDURAS, wx.Layout_LeftToRight,
        "Spanish (Honduras)")
    LNG(wx.LANGUAGE_SPANISH_MEXICAN, "es_MX", LANG_SPANISH, SUBLANG_SPANISH_MEXICAN, wx.Layout_LeftToRight,
        "Spanish (Mexican)")
    LNG(wx.LANGUAGE_SPANISH_MODERN, "es_ES", LANG_SPANISH, SUBLANG_SPANISH_MODERN, wx.Layout_LeftToRight,
        "Spanish (Modern)")
    LNG(wx.LANGUAGE_SPANISH_NICARAGUA, "es_NI", LANG_SPANISH, SUBLANG_SPANISH_NICARAGUA, wx.Layout_LeftToRight,
        "Spanish (Nicaragua)")
    LNG(wx.LANGUAGE_SPANISH_PANAMA, "es_PA", LANG_SPANISH, SUBLANG_SPANISH_PANAMA, wx.Layout_LeftToRight,
        "Spanish (Panama)")
    LNG(wx.LANGUAGE_SPANISH_PARAGUAY, "es_PY", LANG_SPANISH, SUBLANG_SPANISH_PARAGUAY, wx.Layout_LeftToRight,
        "Spanish (Paraguay)")
    LNG(wx.LANGUAGE_SPANISH_PERU, "es_PE", LANG_SPANISH, SUBLANG_SPANISH_PERU, wx.Layout_LeftToRight, "Spanish (Peru)")
    LNG(wx.LANGUAGE_SPANISH_PUERTO_RICO, "es_PR", LANG_SPANISH, SUBLANG_SPANISH_PUERTO_RICO, wx.Layout_LeftToRight,
        "Spanish (Puerto Rico)")
    LNG(wx.LANGUAGE_SPANISH_URUGUAY, "es_UY", LANG_SPANISH, SUBLANG_SPANISH_URUGUAY, wx.Layout_LeftToRight,
        "Spanish (Uruguay)")
    LNG(wx.LANGUAGE_SPANISH_US, "es_US", 0, 0, wx.Layout_LeftToRight, "Spanish (U.S.)")
    LNG(wx.LANGUAGE_SPANISH_VENEZUELA, "es_VE", LANG_SPANISH, SUBLANG_SPANISH_VENEZUELA, wx.Layout_LeftToRight,
        "Spanish (Venezuela)")
    LNG(wx.LANGUAGE_SUNDANESE, "su", 0, 0, wx.Layout_LeftToRight, "Sundanese")
    LNG(wx.LANGUAGE_SWAHILI, "sw_KE", LANG_SWAHILI, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Swahili")
    LNG(wx.LANGUAGE_SWEDISH, "sv_SE", LANG_SWEDISH, SUBLANG_SWEDISH, wx.Layout_LeftToRight, "Swedish")
    LNG(wx.LANGUAGE_SWEDISH_FINLAND, "sv_FI", LANG_SWEDISH, SUBLANG_SWEDISH_FINLAND, wx.Layout_LeftToRight,
        "Swedish (Finland)")
    LNG(wx.LANGUAGE_TAGALOG, "tl_PH", 0, 0, wx.Layout_LeftToRight, "Tagalog")
    LNG(wx.LANGUAGE_TAJIK, "tg", 0, 0, wx.Layout_LeftToRight, "Tajik")
    LNG(wx.LANGUAGE_TAMIL, "ta", LANG_TAMIL, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Tamil")
    LNG(wx.LANGUAGE_TATAR, "tt", LANG_TATAR, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Tatar")
    LNG(wx.LANGUAGE_TELUGU, "te", LANG_TELUGU, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Telugu")
    LNG(wx.LANGUAGE_THAI, "th_TH", LANG_THAI, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Thai")
    LNG(wx.LANGUAGE_TIBETAN, "bo", 0, 0, wx.Layout_LeftToRight, "Tibetan")
    LNG(wx.LANGUAGE_TIGRINYA, "ti", 0, 0, wx.Layout_LeftToRight, "Tigrinya")
    LNG(wx.LANGUAGE_TONGA, "to", 0, 0, wx.Layout_LeftToRight, "Tonga")
    LNG(wx.LANGUAGE_TSONGA, "ts", 0, 0, wx.Layout_LeftToRight, "Tsonga")
    LNG(wx.LANGUAGE_TURKISH, "tr_TR", LANG_TURKISH, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Turkish")
    LNG(wx.LANGUAGE_TURKMEN, "tk", 0, 0, wx.Layout_LeftToRight, "Turkmen")
    LNG(wx.LANGUAGE_TWI, "tw", 0, 0, wx.Layout_LeftToRight, "Twi")
    LNG(wx.LANGUAGE_UIGHUR, "ug", 0, 0, wx.Layout_LeftToRight, "Uighur")
    LNG(wx.LANGUAGE_UKRAINIAN, "uk_UA", LANG_UKRAINIAN, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Ukrainian")
    LNG(wx.LANGUAGE_URDU, "ur", LANG_URDU, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Urdu")
    LNG(wx.LANGUAGE_URDU_INDIA, "ur_IN", LANG_URDU, SUBLANG_URDU_INDIA, wx.Layout_LeftToRight, "Urdu (India)")
    LNG(wx.LANGUAGE_URDU_PAKISTAN, "ur_PK", LANG_URDU, SUBLANG_URDU_PAKISTAN, wx.Layout_LeftToRight, "Urdu (Pakistan)")
    LNG(wx.LANGUAGE_UZBEK, "uz", LANG_UZBEK, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Uzbek")
    LNG(wx.LANGUAGE_UZBEK_CYRILLIC, "uz", LANG_UZBEK, SUBLANG_UZBEK_CYRILLIC, wx.Layout_LeftToRight, "Uzbek (Cyrillic)")
    LNG(wx.LANGUAGE_UZBEK_LATIN, "uz", LANG_UZBEK, SUBLANG_UZBEK_LATIN, wx.Layout_LeftToRight, "Uzbek (Latin)")
    LNG(wx.LANGUAGE_VALENCIAN, "ca_ES@valencia", 0, 0, wx.Layout_LeftToRight, "Valencian (Southern Catalan)")
    LNG(wx.LANGUAGE_VIETNAMESE, "vi_VN", LANG_VIETNAMESE, SUBLANG_DEFAULT, wx.Layout_LeftToRight, "Vietnamese")
    LNG(wx.LANGUAGE_VOLAPUK, "vo", 0, 0, wx.Layout_LeftToRight, "Volapuk")
    LNG(wx.LANGUAGE_WELSH, "cy", 0, 0, wx.Layout_LeftToRight, "Welsh")
    LNG(wx.LANGUAGE_WOLOF, "wo", 0, 0, wx.Layout_LeftToRight, "Wolof")
    LNG(wx.LANGUAGE_XHOSA, "xh", 0, 0, wx.Layout_LeftToRight, "Xhosa")
    LNG(wx.LANGUAGE_YIDDISH, "yi", 0, 0, wx.Layout_LeftToRight, "Yiddish")
    LNG(wx.LANGUAGE_YORUBA, "yo", 0, 0, wx.Layout_LeftToRight, "Yoruba")
    LNG(wx.LANGUAGE_ZHUANG, "za", 0, 0, wx.Layout_LeftToRight, "Zhuang")
    LNG(wx.LANGUAGE_ZULU, "zu", 0, 0, wx.Layout_LeftToRight, "Zulu")


class Locale(_Locale):
    m_pszOldLocale = None
    m_pOldLocale = None
    ms_languagesDB = None

    def __init__(self, *args, **kwargs):
        global _current_locale
        if not args and not kwargs:
            kwargs['iso_code'] = Locale.GetSystemLanguage().replace('-', '_')

        super(Locale, self).__init__()

        self.DoCommonInit()

        self.m_strShort = ''
        self.m_strLocale = ''
        self.m_language = ''
        self.m_initialized = False
        self.m_translations = None

        if args or kwargs:
            if self.Init(*args, **kwargs):
                _current_locale = self

    @staticmethod
    def DestroyLanguagesDB():
        if Locale.ms_languagesDB is not None:
            del Locale.ms_languagesDB[:]
            Locale.ms_languagesDB = None

    @staticmethod
    def CreateLanguagesDB():
        if Locale.ms_languagesDB is None:
            Locale.ms_languagesDB = []
            Locale.InitLanguagesDB()

    @staticmethod
    def InitLanguagesDB():
        _add_languages_to_db()

    @staticmethod
    def AddCatalog(*args, **kwargs):
        return _Locale.AddCatalog(*args, **kwargs)

    @staticmethod
    def AddCatalogLookupPathPrefix(*args, **kwargs):
        return _Locale.AddCatalogLookupPathPrefix(*args, **kwargs)

    @staticmethod
    def AddLanguage(info):
        Locale.CreateLanguagesDB()
        Locale.ms_languagesDB += [info]

    @staticmethod
    def FindLanguageInfo(lang):
        Locale.CreateLanguagesDB()

        for info in Locale.ms_languagesDB:
            if lang in (info.CanonicalName, info.Language, info.CanonicalName.split('_')[0]):
                return info

    def GetCanonicalName(self):
        return self.m_strShort

    def GetHeaderValue(self, *args, **kwargs):
        return super(Locale, self).GetHeaderValue(*args, **kwargs)

    @staticmethod
    def GetLanguageInfo(lang):
        Locale.CreateLanguagesDB()

        if lang == wx.LANGUAGE_DEFAULT:
            lang = Locale.GetSystemLanguage()

        for info in Locale.ms_languagesDB:
            if info.Language == lang:
                return info

    @staticmethod
    def GetInfo(index, cat=wx.LOCALE_CAT_DEFAULT):
        locale = wx.GetLocale()

        if locale:
            info = Locale.FindLanguageInfo(locale.GetLanguage())
        else:
            info = None

        def get_defaults():
            if index == wx.LOCALE_THOUSANDS_SEP:
                return ''
            if index == wx.LOCALE_DECIMAL_POINT:
                return '.'
            if index == wx.LOCALE_SHORT_DATE_FMT:
                return '%m/%d/%y'
            if index == wx.LOCALE_LONG_DATE_FMT:
                return '%A, %B %d, %Y'
            if index == wx.LOCALE_TIME_FMT:
                return '%H:%M:%S'
            if index == wx.LOCALE_DATE_TIME_FMT:
                return '%m/%d/%y %H:%M:%S'

            raise RuntimeError

        if info is None:
            return get_defaults()

        res = GetLocaleInfo(info.GetFullLocaleName(locale), index, cat)

        if not res and index in (
            wx.LOCALE_SHORT_DATE_FMT,
            wx.LOCALE_LONG_DATE_FMT,
            wx.LOCALE_TIME_FMT,
            wx.LOCALE_DATE_TIME_FMT
        ):
            return get_defaults()

        return res

    def GetLanguage(self):
        return self.m_language

    @staticmethod
    def GetLanguageCanonicalName(lang):
        if lang in (wx.LANGUAGE_DEFAULT, wx.LANGUAGE_UNKNOWN):
            return ''

        lang_info = Locale.GetLanguageInfo(lang)
        if lang_info:
            return lang_info.CanonicalName

        return ''

    @staticmethod
    def GetLanguageName(lang):
        if lang in (wx.LANGUAGE_DEFAULT, wx.LANGUAGE_UNKNOWN):
            return ''

        lang_info = Locale.GetLanguageInfo(lang)
        if lang_info:
            return lang_info.Description

        return ''

    @staticmethod
    def GetOSInfo(index, cat):
        return GetInfoFromLCID(GetThreadLocale(), index, cat)

    def GetLocale(self):
        if self.m_strShort:
            return self.m_strShort
        else:
            return super(Locale, self).GetLocale()

    def GetName(self):
        return self.m_strLocale

    def GetString(self, *args, **kwargs):
        return super(Locale, self).GetString(*args, **kwargs)

    def GetSysName(self):
        return wx.Setlocale(LC_ALL, None)

    @staticmethod
    def GetSystemEncoding():
        locale = wx.GetLocale()
        info = Locale.FindLanguageInfo(locale.GetLanguage())
        iso_code = info.GetFullLocaleName(locale)
        default_ansi_codepage = GetLocaleInfoEx(iso_code, LOCALE_IDEFAULTANSICODEPAGE)

        if default_ansi_codepage in list(range(1250, 1259)):
            return wx.FONTENCODING_CP1250 + default_ansi_codepage - 1250

        mapping = {
            1361: wxFONTENCODING_CP1361,
            874: wxFONTENCODING_CP874,
            932: wxFONTENCODING_CP932,
            936: wxFONTENCODING_CP936,
            949: wxFONTENCODING_CP949,
            950: wxFONTENCODING_CP950,
            65001: wxFONTENCODING_UTF8
        }
        if default_ansi_codepage in mapping:
            return mapping[default_ansi_codepage]

        return wx.FONTENCODING_SYSTEM

    @staticmethod
    def GetSystemEncodingName():
        locale = wx.GetLocale()
        info = Locale.FindLanguageInfo(locale.GetLanguage())
        iso_code = info.GetFullLocaleName(locale)
        default_ansi_codepage = GetLocaleInfoEx(iso_code, LOCALE_IDEFAULTANSICODEPAGE)
        return CODE_PAGES[default_ansi_codepage]

    @staticmethod
    def GetSystemLanguage():
        return GetThreadUILanguage()

    def DoInit(self, name, shortName, language):
        assert not self.m_initialized, "you can't call wxLocale::Init more than once"

        self.m_initialized = True
        self.m_strLocale = name
        self.m_strShort = shortName
        self.m_language = language

    def DoCommonInit(self):
        Locale.m_pszOldLocale = wx.Setlocale(LC_ALL, None)
        Locale.m_pOldLocale = wx.GetLocale()

        oldTrans = wx.Translations.Get()
        if (
            not oldTrans or
            (Locale.m_pOldLocale and oldTrans == getattr(Locale.m_pOldLocale, 'm_translations', None))
        ):
            wx.Translations.SetNonOwned(self.m_translations)

        self.m_language = wx.LANGUAGE_UNKNOWN
        self.m_initialized = False

    def DoCommonPostInit(self, success, name, shortName, bLoadDefault):
        t = wx.Translations.Get()
        if t:
            t.SetLanguage(shortName)

            if bLoadDefault:
                t.AddStdCatalog()
        return success

    @property
    def LocalizedDescription(self):
        info = self.FindLanguageInfo(self.m_language)
        return GetLocaleInfoEx(info.GetFullLocaleName(self), LOCALE_SLOCALIZEDCOUNTRYNAME)

    @property
    def NativeDescription(self):
        info = self.FindLanguageInfo(self.m_language)
        return GetLocaleInfoEx(info.GetFullLocaleName(self), LOCALE_SNATIVECOUNTRYNAME)

    @property
    def Description(self):
        info = self.FindLanguageInfo(self.m_language)
        return GetLocaleInfoEx(info.GetFullLocaleName(self), LOCALE_SENGLISHCOUNTRYNAME)

    def Init(self, *args, **kwargs):
        args = list(args)

        if len(args) == 1:
            iso_code = args.pop(0)
            lang, locale = iso_code.replace('_', '-').split('-', 1)
            info = self.FindLanguageInfo(lang)

            if not info:
                info = self.FindLanguageInfo(iso_code.replace('-', '_'))
            if not info:
                LNG(wx.LANGUAGE_USER_DEFINED, lang, 0, 0, 0, '')
                info = self.FindLanguageInfo(lang)

            success = True
            name = info.Description
            shortName = info.CanonicalName
            bLoadDefault = False
            self.DoInit(name, info.CanonicalName, lang)
            szLocale = lang + '_' + locale

        elif 'iso_code' in kwargs:
            iso_code = kwargs['iso_code']
            lang, locale = iso_code.replace('_', '-').split('-', 1)
            info = self.FindLanguageInfo(iso_code.replace('-', '_'))

            if not info:
                info = self.FindLanguageInfo(lang)
            if not info:
                LNG(wx.LANGUAGE_USER_DEFINED, lang, 0, 0, 0, '')
                info = self.FindLanguageInfo(lang)

            success = True
            name = GetLocaleInfoEx(iso_code.replace('_', '-'), LOCALE_SENGLISHCOUNTRYNAME)

            shortName = locale
            bLoadDefault = False
            self.DoInit(name, shortName, lang)

            szLocale = lang + '_' + locale

        elif len(args):
            if isinstance(args[0], int):
                language = args.pop(0)

                if len(args):
                    flags = args.pop(0)
                else:
                    flags = kwargs.get('flags')

                if language == wx.LANGUAGE_DEFAULT:
                    lang = self.GetSystemLanguage()
                else:
                    lang = language

                if lang == wx.LANGUAGE_UNKNOWN:
                    return False

                info = self.GetLanguageInfo(lang)
                if not info:
                    return False

                name = info.Description
                self.DoInit(name, info.CanonicalName, lang)

                if info.WinLang != 0:
                    lcid = info.GetLCID()
                    SetThreadLocale(lcid)

                    if wx.GetWinVersion() >= wx.WinVersion_Vista:
                        SetThreadUILanguage(LANGIDFROMLCID(lcid))

                success = info.TrySetLocale() is not None

                if language == wx.LANGUAGE_DEFAULT:
                    shortName = ''
                else:
                    shortName = info.CanonicalName

                bLoadDefault = bool(flags & wx.LOCALE_LOAD_DEFAULT)
                szLocale = shortName
            else:
                name = args.pop(0)
                if len(args):
                    shortName = args.pop(0)
                else:
                    shortName = kwargs.get('shortName')

                if len(args):
                    locale = args.pop(0)
                else:
                    locale = kwargs.get('locale')

                if len(args):
                    bLoadDefault = args.pop(0)
                else:
                    bLoadDefault = kwargs.get('bLoadDefault')

                if locale:
                    szLocale = locale
                else:
                    szLocale = shortName

                info = self.FindLanguageInfo(szLocale)
                if info.CanonicalName.StartsWith(shortName):
                    if bLoadDefault:
                        flags = wx.LOCALE_LOAD_DEFAULT
                    else:
                        flags = 0

                    return self.Init(info.Language, flags)

                if shortName:
                    strShort = shortName.upper()
                elif szLocale:
                    strShort = szLocale[-2:].upper()
                else:
                    strShort = ''

                self.DoInit(name, strShort, wx.LANGUAGE_UNKNOWN)

                success = wx.Setlocale(LC_ALL, szLocale) is not None
                name = szLocale

        elif 'language' in kwargs:
            language = kwargs.get('language')
            flags = kwargs.get('flags')

            if language == wx.LANGUAGE_DEFAULT:
                lang = Locale.GetSystemLanguage()
            else:
                lang = language

            if lang == wx.LANGUAGE_UNKNOWN:
                return False

            info = self.GetLanguageInfo(lang)
            if not info:
                return False

            name = info.Description
            self.DoInit(name, info.CanonicalName, lang)

            if info.WinLang != 0:
                lcid = info.GetLCID()
                SetThreadLocale(lcid)

                if wx.GetWinVersion() >= wx.WinVersion_Vista:
                    SetThreadUILanguage(LANGIDFROMLCID(lcid))

            success = info.TrySetLocale() is not None
            if language == wx.LANGUAGE_DEFAULT:
                shortName = ''
            else:
                shortName = info.CanonicalName

            bLoadDefault = bool(flags & wx.LOCALE_LOAD_DEFAULT)
            szLocale = shortName

        else:
            name = kwargs.get('name')
            shortName = kwargs.get('shortName')
            locale = kwargs.get('locale')
            bLoadDefault = kwargs.get('bLoadDefault')

            if locale:
                szLocale = locale
            else:
                szLocale = shortName

            info = self.FindLanguageInfo(szLocale)
            if info.CanonicalName.StartsWith(shortName):
                if bLoadDefault:
                    flags = wx.LOCALE_LOAD_DEFAULT
                else:
                    flags = 0

                return self.Init(info.Language, flags)

            if shortName:
                strShort = shortName.upper()
            elif szLocale:
                strShort = szLocale[-2:].upper()
            else:
                strShort = ''

            self.DoInit(name, strShort, wx.LANGUAGE_UNKNOWN)

            success = wx.Setlocale(LC_ALL, szLocale) is not None
            name = szLocale

        self.DoCommonPostInit(success, name, shortName, bLoadDefault)

        try:
            szLocale = szLocale.replace('_', '-')
            _locale.setlocale(LC_ALL, szLocale)
            if PY3:
                szLocale = szLocale.encode('utf-8')
            if not wx.Setlocale(LC_ALL, szLocale):
                return False
        except _locale.Error:
            try:
                locale_string = info.GetANSIName(self)
                if not PY3:
                    locale_string = locale_string.encode('utf-8')

                _locale.setlocale(LC_ALL, locale_string)
                if not wx.Setlocale(LC_ALL, locale_string):
                    return False
            except _locale.Error:
                try:
                    lcid = LocaleNameToLCID(szLocale)
                    _locale.setlocale(LC_ALL, lcid)
                    if not wx.Setlocale(LC_ALL, lcid):
                        raise RuntimeError
                except _locale.Error:
                    raise
        return True

    @staticmethod
    def IsAvailable(lang):
        if isinstance(lang, int):
            info = Locale.GetLanguageInfo(lang)

            if info is None:
                return False
            if not info.WinLang:
                return False

            lcid = info.GetLCID()
        else:
            if '-' in lang or '_' in lang:
                iso_code = lang.replace('_', '-')
                lang = iso_code.split('-')[0]
                info = Locale.FindLanguageInfo(lang)
                if info is None:
                    lang = LNG(wx.LANGUAGE_USER_DEFINED, lang, 0, 0, 0, '')
                    info = Locale.FindLanguageInfo(lang)
            else:
                info = Locale.FindLanguageInfo(lang)
                if info is None:
                    lang = LNG(wx.LANGUAGE_USER_DEFINED, lang, 0, 0, 0, lang)
                    info = Locale.FindLanguageInfo(lang)

            iso_code = info.GetFullLocaleName(wx.GetLocale())

            lcid = LocaleNameToLCID(iso_code)

        if lcid is None:
            return False

        return IsValidLocale(lcid)

    def IsLoaded(self, *args, **kwargs):
        return super(Locale, self).IsLoaded(*args, **kwargs)

    def IsOk(self):
        return self.m_pszOldLocale is not None

    Language = property(fget=GetLanguage)
    Locale = property(fget=GetLocale)
    Name = property(fget=GetName)
    SysName = property(fget=GetSysName)
    CanonicalName = property(fget=GetCanonicalName)


class LanguageInfo(wx.LanguageInfo):

    def __init__(self):
        super(LanguageInfo, self).__init__()
        self._CanonicalName = ''
        self._Language = None
        self._LayoutDirection = None
        self._LocaleName = ''
        self._WinLang = 0
        self._WinSublang = 0

    @property
    def CanonicalName(self):
        return self._CanonicalName

    @CanonicalName.setter
    def CanonicalName(self, value):
        self._CanonicalName = value.split('_')[0]

    @property
    def Language(self):
        return self._Language

    @Language.setter
    def Language(self, value):
        self._Language = value

    @property
    def LanguageDirection(self):
        return self._LayoutDirection

    @LanguageDirection.setter
    def LanguageDirection(self, value):
        self._LayoutDirection = value

    @property
    def LocaleName(self):
        locale = wx.GetLocale()
        return self.GetFullLocaleName(locale).replace('-', '_')

    @LocaleName.setter
    def LocaleName(self, value):
        self._LocaleName = value

    @property
    def WinLang(self):
        return self._WinLang

    @WinLang.setter
    def WinLang(self, value):
        self._WinLang = value

    @property
    def WinSublang(self):
        return self._WinSublang

    @WinSublang.setter
    def WinSublang(self, value):
        self._WinSublang = value

    @property
    def LocalizedDescription(self):
        return GetLocaleInfoEx(
            self.GetFullLocaleName(wx.GetLocale()),
            LOCALE_SLOCALIZEDLANGUAGENAME
        )

    @property
    def NativeDescription(self):
        return GetLocaleInfoEx(
            self.GetFullLocaleName(wx.GetLocale()),
            LOCALE_SNATIVELANGUAGENAME
        )

    @property
    def Description(self):
        return GetLocaleInfoEx(
            self.GetFullLocaleName(wx.GetLocale()),
            LOCALE_SENGLISHLANGUAGENAME
        )

    @Description.setter
    def Description(self, _):
        pass

    def GetLocaleName(self):
        orig = wx.Setlocale(LC_ALL, None)
        ret = self.TrySetLocale()

        if ret:
            wx.Setlocale(LC_ALL, orig)
            _locale.setlocale(LC_ALL, orig)
            return ret

        return ''

    def GetFullLocaleName(self, locale):
        locale_iso = locale.GetLocale()

        if (
            not locale_iso and
            ('_' in self.CanonicalName or '-' in self.CanonicalName)
        ):
            locale_iso = self.CanonicalName.replace('_', '-').split('-', 1)[-1]

        lang_iso = self.CanonicalName.split('_')[0]
        iso_code = lang_iso + '-' + locale_iso
        return iso_code

    def GetANSIName(self, locale):
        english_language_name = GetLocaleInfoEx(
            self.GetFullLocaleName(locale),
            LOCALE_SENGLISHLANGUAGENAME
        )

        english_locale_name = locale.Description
        locale_iso = locale.GetLocale()

        if (
            not locale_iso and
            ('_' in self.CanonicalName or '-' in self.CanonicalName)
        ):
            locale_iso = self.CanonicalName.replace('_', '-').split('-', 1)[-1]

        lang_iso = self.CanonicalName.split('_')[0]
        iso_code = lang_iso + '-' + locale_iso

        default_ansi_codepage = GetLocaleInfoEx(
            iso_code,
            LOCALE_IDEFAULTANSICODEPAGE
        )

        if english_language_name and english_locale_name:
            locale_string = english_language_name + '_' + english_locale_name
        else:
            locale_string = iso_code.replace('-', '_')

        if default_ansi_codepage in CODE_PAGES:
            locale_string += '.' + CODE_PAGES[default_ansi_codepage]

        return locale_string

    def TrySetLocale(self):
        locale = wx.GetLocale()
        try:
            iso_code = self.GetFullLocaleName(locale)
            _locale.setlocale(LC_ALL, iso_code)

            if wx.Setlocale(LC_ALL, iso_code) != iso_code:
                raise ValueError

            return iso_code

        except (ValueError, _locale.Error):
            locale_string = self.GetANSIName(locale)
            _locale.setlocale(LC_ALL, locale_string)

            if not wx.Setlocale(LC_ALL, locale_string):
                raise ValueError

            return locale_string

    def GetLCID(self):
        locale = wx.GetLocale()
        locale_iso = locale.GetLocale()
        lang_iso = self.CanonicalName.split('_')[0]
        iso_code = lang_iso + '-' + locale_iso
        return LocaleNameToLCID(iso_code)

import wx._core

_get_locale = wx.GetLocale

wx._core.Locale = Locale
wx.Locale = Locale
wx.LanguageInfo = LanguageInfo

sys.modules['wx'].Locale = Locale
sys.modules['wx'].LanguageInfo = LanguageInfo


_current_locale = Locale()


def GetLocale():
    return _current_locale

wx.GetLocale = GetLocale


if __name__ == '__main__':
    import time
    from ctypes.wintypes import LPARAM, LPWSTR
    LOCALE_WINDOWS = 1
    LOCALE_SENGLISHLANGUAGENAME = 0x1001
    LOCALE_SENGLISHCOUNTRYNAME = 0x1002
    LOCALE_IDEFAULTANSICODEPAGE = 0x1004
    LCTYPES = (LOCALE_SENGLISHLANGUAGENAME,
               LOCALE_SENGLISHCOUNTRYNAME,
               LOCALE_IDEFAULTANSICODEPAGE)

    EnumSystemLocalesEx = _kernel32.EnumSystemLocalesEx

    EnumLocalesProcEx = ctypes.WINFUNCTYPE(BOOL, LPWSTR, DWORD, LPARAM)


    def enum_system_locales():
        alias = {}
        codepage = {}

        @EnumLocalesProcEx
        def callback(locale, flags, param):
            if '-' not in locale:
                return True
            parts = []
            for lctype in LCTYPES:
                info = GetLocaleInfoEx(locale, lctype)
                parts.append(info)
            lang, ctry, code = parts
            if lang and ctry and code != '0':
                locale = locale.replace('-', '_')
                full = u'{}_{}'.format(lang, ctry)
                alias[full] = locale
                codepage[locale] = code
            return True

        if not EnumSystemLocalesEx(callback,
                                   LOCALE_WINDOWS,
                                   None, None):
            raise WinError()
        return alias, codepage


    app = wx.App()

    a, cps = enum_system_locales()
    count = 0
    # for some crazy bat shit reason I am not able to figure out I have to have
    # exactly 4 pauses (sleeps) when running this demo. If they are not there I
    # get an application crash. I know it has something to do with wx.Setlocale
    # because if I remove the use of it the problem goes away.
    # I do not believe that wx.Setlocale even needs to be called if I am calling
    # locale.setlocale in Python. I am not sure how to go about testing this theory.
    # maybe someone can shed some light on it.

    for als, iso in a.items():
        lcl = wx.Locale(iso_code=iso)
        print('=' * 80)
        print('locale english description:', lcl.Description)
        print('locale native description:', lcl.NativeDescription)
        print('locale localized description:', lcl.LocalizedDescription)
        lng_info = lcl.FindLanguageInfo(lcl.GetLanguage())
        #
        print('language english description:', lng_info.Description)
        time.sleep(0.000001)
        print('language native description:', lng_info.NativeDescription)
        time.sleep(0.000001)
        print('language localized description:', lng_info.LocalizedDescription)
        time.sleep(0.000001)
        print('full iso locale:', lng_info.GetFullLocaleName(lcl))
        time.sleep(0.000001)
        print('ansi code page locale:', lng_info.GetANSIName(lcl))

        for ag_name, ags in (
            ('LOCALE_THOUSANDS_SEP', (wx.LOCALE_THOUSANDS_SEP,)),
            ('LOCALE_CAT_MONEY', (wx.LOCALE_DECIMAL_POINT, wx.LOCALE_CAT_MONEY)),
            ('LOCALE_DECIMAL_POINT', (wx.LOCALE_DECIMAL_POINT,)),
            ('LOCALE_SHORT_DATE_FMT', (wx.LOCALE_SHORT_DATE_FMT,)),
            ('LOCALE_LONG_DATE_FMT', (wx.LOCALE_LONG_DATE_FMT,)),
            ('LOCALE_TIME_FMT', (wx.LOCALE_TIME_FMT,)),
            ('LOCALE_DATE_TIME_FMT', (wx.LOCALE_DATE_TIME_FMT,))
        ):

            print(ag_name + ':', lcl.GetInfo(*ags))

        print('=' * 80)
        print()
        count += 1

    print('supported language/locale combinations:', count)
