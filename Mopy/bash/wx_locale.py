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
import locale as _locale
import sys
from ctypes.wintypes import DWORD, BOOL

import wx

from ._wx_lang_codes import LNGINFO, _add_languages_to_db, LanguageInfo, \
    LOCALE_SENGLISHCOUNTRYNAME, LOCALE_IDEFAULTANSICODEPAGE, \
    LOCALE_SNATIVECOUNTRYNAME, LOCALE_SLOCALIZEDCOUNTRYNAME, LC_ALL, CODE_PAGES
from ._wx_locale_functions import GetLocaleInfoEx, SetThreadUILanguage, \
    IsValidLocale, GetThreadUILanguage, LocaleNameToLCID, LANGIDFROMLCID, \
    LOCALE_STHOUSAND, LOCALE_SMONDECIMALSEP, LOCALE_SDECIMAL, \
    LOCALE_SSHORTDATE, LOCALE_SLONGDATE, LOCALE_STIMEFORMAT, \
    EnumSystemLocalesEx, SetThreadLocale

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

class Locale(wx.Locale):
    m_pszOldLocale = None
    m_pOldLocale = None
    ms_languagesDB = None

    def __init__(self, *args, **kwargs):
        if not args and not kwargs:
            kwargs['iso_code'] = Locale.GetSystemLanguage().replace('-', '_')
        super(Locale, self).__init__()
        self._do_common_init()
        self.m_strShort = ''
        self.m_strLocale = ''
        self.m_language = ''
        self.m_initialized = False
        self.m_translations = None
        if args or kwargs:
            if self.Init(*args, **kwargs):
                global _current_locale
                _current_locale = self

    # Init override and helpers -----------------------------------------------
    def Init(self, *args, **kwargs):
        args = list(args)
        if len(args) == 1:
            iso_code = args.pop(0)
            lang, locale = iso_code.replace('_', '-').split('-', 1)
            info = self.FindLanguageInfo(lang)
            if not info:
                info = self.FindLanguageInfo(iso_code.replace('-', '_'))
            if not info:
                LNGINFO(wx.LANGUAGE_USER_DEFINED, lang, 0, 0, 0, '', Locale)
                info = self.FindLanguageInfo(lang)
            success = True
            name = info.Description
            shortName = info.CanonicalName
            bLoadDefault = False
            self._do_init(name, info.CanonicalName, lang)
            szLocale = lang + '_' + locale
        elif 'iso_code' in kwargs:
            iso_code = kwargs['iso_code']
            lang, locale = iso_code.replace('_', '-').split('-', 1)
            info = self.FindLanguageInfo(iso_code.replace('-', '_'))
            if not info:
                info = self.FindLanguageInfo(lang)
            if not info:
                LNGINFO(wx.LANGUAGE_USER_DEFINED, lang, 0, 0, 0, '', Locale)
                info = self.FindLanguageInfo(lang)
            success = True
            name = GetLocaleInfoEx(iso_code.replace('_', '-'), LOCALE_SENGLISHCOUNTRYNAME)
            shortName = locale
            bLoadDefault = False
            self._do_init(name, shortName, lang)
            szLocale = lang + '_' + locale
        elif args:
            if isinstance(args[0], int):
                language = args.pop(0)
                if args:
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
                self._do_init(name, info.CanonicalName, lang)
                if info.WinLang != 0:
                    lcid = info.GetLCID()
                    SetThreadLocale(lcid)
                    SetThreadUILanguage(LANGIDFROMLCID(lcid))
                success = info.TrySetLocale() is not None
                shortName = '' if language == wx.LANGUAGE_DEFAULT else \
                    info.CanonicalName
                bLoadDefault = bool(flags & wx.LOCALE_LOAD_DEFAULT)
                szLocale = shortName
            else:
                name = args.pop(0)
                shortName = args.pop(0) if args else kwargs.get('shortName')
                locale = args.pop(0) if args else kwargs.get('locale')

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

                self._do_init(name, strShort, wx.LANGUAGE_UNKNOWN)

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
            self._do_init(name, info.CanonicalName, lang)
            if info.WinLang != 0:
                lcid = info.GetLCID()
                SetThreadLocale(lcid)
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
            self._do_init(name, strShort, wx.LANGUAGE_UNKNOWN)
            success = wx.Setlocale(LC_ALL, szLocale) is not None
            name = szLocale
        self._do_common_post_init(success, name, shortName, bLoadDefault)
        try:
            szLocale = szLocale.replace('_', '-')
            _locale.setlocale(LC_ALL, szLocale)
            szLocale = szLocale.encode('utf-8')
            if not wx.Setlocale(LC_ALL, szLocale):
                return False
        except _locale.Error:
            try:
                locale_string = info.GetANSIName(self)
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

    def _do_common_init(self):
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

    def _do_common_post_init(self, success, name, shortName, bLoadDefault):
        t = wx.Translations.Get()
        if t:
            t.SetLanguage(shortName)
            if bLoadDefault:
                t.AddStdCatalog()
        return success

    # Language database overrides and helpers
    @classmethod
    def _create_language_db(cls):
        if cls.ms_languagesDB is None:
            cls.ms_languagesDB = []
            _add_languages_to_db(cls)

    @staticmethod
    def AddLanguage(info):
        try:
            Locale.ms_languagesDB += [info]
        except TypeError:
            if Locale.ms_languagesDB is None:
                Locale._create_language_db()
                return Locale.AddLanguage(info)
            raise

    @staticmethod
    def FindLanguageInfo(lang):
        try:
            for info in Locale.ms_languagesDB:
                if lang in (info.CanonicalName, info.Language, info.CanonicalName.split('_')[0]):
                    return info
        except TypeError:
            if Locale.ms_languagesDB is None:
                Locale._create_language_db()
                return Locale.FindLanguageInfo(lang)
            raise

    @staticmethod
    def GetLanguageInfo(lang):
        try:
            if lang == wx.LANGUAGE_DEFAULT:
                lang = Locale.GetSystemLanguage()
            for info in Locale.ms_languagesDB:
                if info.Language == lang:
                    return info
        except TypeError:
            if Locale.ms_languagesDB is None:
                Locale._create_language_db()
                return Locale.FindLanguageInfo(lang)
            raise

    _defaults_dict = {
        wx.LOCALE_THOUSANDS_SEP: '',
        wx.LOCALE_DECIMAL_POINT: '.',
        wx.LOCALE_SHORT_DATE_FMT: '%m/%d/%y',
        wx.LOCALE_LONG_DATE_FMT: '%A, %B %d, %Y',
        wx.LOCALE_TIME_FMT: '%H:%M:%S',
        wx.LOCALE_DATE_TIME_FMT: '%m/%d/%y %H:%M:%S',
    }
    @staticmethod
    def GetInfo(index, cat=wx.LOCALE_CAT_DEFAULT):
        locale = wx.GetLocale()
        if not locale:
            return Locale._defaults_dict[index]
        info = Locale.FindLanguageInfo(locale.GetLanguage())
        res = GetLocaleInfo(info.GetFullLocaleName(locale), index, cat)
        if not res and index in (
            wx.LOCALE_SHORT_DATE_FMT,
            wx.LOCALE_LONG_DATE_FMT,
            wx.LOCALE_TIME_FMT,
            wx.LOCALE_DATE_TIME_FMT
        ):
            return Locale._defaults_dict[index]
        return res

    # Property overrides ------------------------------------------------------
    def GetLanguage(self):
        return self.m_language

    def GetLocale(self):
        return self.m_strShort if self.m_strShort else super(Locale,
                                                             self).GetLocale()

    def GetName(self):
        return self.m_strLocale

    def GetSysName(self):
        return wx.Setlocale(LC_ALL, None)

    def GetCanonicalName(self):
        return self.m_strShort

    Language = property(fget=GetLanguage)
    Locale = property(fget=GetLocale)
    Name = property(fget=GetName)
    SysName = property(fget=GetSysName)
    CanonicalName = property(fget=GetCanonicalName)

    # New properties ----------------------------------------------------------
    @property
    def NativeDescription(self):
        info = self.FindLanguageInfo(self.m_language)
        return GetLocaleInfoEx(info.GetFullLocaleName(self),
                               LOCALE_SNATIVECOUNTRYNAME)

    @property
    def Description(self):
        info = self.FindLanguageInfo(self.m_language)
        return GetLocaleInfoEx(info.GetFullLocaleName(self),
                               LOCALE_SENGLISHCOUNTRYNAME)

    @property
    def LocalizedDescription(self):
        info = self.FindLanguageInfo(self.m_language)
        return GetLocaleInfoEx(info.GetFullLocaleName(self),
                               LOCALE_SLOCALIZEDCOUNTRYNAME)

    # Static methods overrides ------------------------------------------------
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
        raise NotImplementedError # missing defs of GetInfoFromLCID GetThreadLocale
        return GetInfoFromLCID(GetThreadLocale(), index, cat)

    @staticmethod
    def GetSystemEncoding():
        locale = wx.GetLocale()
        info = Locale.FindLanguageInfo(locale.GetLanguage())
        iso_code = info.GetFullLocaleName(locale)
        default_ansi_codepage = GetLocaleInfoEx(iso_code, LOCALE_IDEFAULTANSICODEPAGE)
        if default_ansi_codepage in list(range(1250, 1259)):
            return wx.FONTENCODING_CP1250 + default_ansi_codepage - 1250
        mapping = {
            1361: wx.FONTENCODING_CP1361,
            874: wx.FONTENCODING_CP874,
            932: wx.FONTENCODING_CP932,
            936: wx.FONTENCODING_CP936,
            949: wx.FONTENCODING_CP949,
            950: wx.FONTENCODING_CP950,
            65001: wx.FONTENCODING_UTF8
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

    def _do_init(self, name, shortName, language):
        assert not self.m_initialized, "you can't call wxLocale::Init more than once"

        self.m_initialized = True
        self.m_strLocale = name
        self.m_strShort = shortName
        self.m_language = language

    @staticmethod
    def IsAvailable(lang):
        if isinstance(lang, int):
            info = Locale.GetLanguageInfo(lang)
            if info is None or not info.WinLang:
                return False
            lcid = info.GetLCID()
        else:
            if '-' in lang or '_' in lang:
                iso_code = lang.replace('_', '-')
                lang = iso_code.split('-')[0]
                info = Locale.FindLanguageInfo(lang)
                if info is None:
                    lang = LNGINFO(wx.LANGUAGE_USER_DEFINED, lang, 0, 0, 0, '', Locale)
                    info = Locale.FindLanguageInfo(lang)
            else:
                info = Locale.FindLanguageInfo(lang)
                if info is None:
                    lang = LNGINFO(wx.LANGUAGE_USER_DEFINED, lang, 0, 0, 0, lang, Locale)
                    info = Locale.FindLanguageInfo(lang)

            iso_code = info.GetFullLocaleName(wx.GetLocale())

            lcid = LocaleNameToLCID(iso_code)

        if lcid is None:
            return False

        return IsValidLocale(lcid)

    def IsOk(self):
        return self.m_pszOldLocale is not None

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
            raise ctypes.WinError()
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
