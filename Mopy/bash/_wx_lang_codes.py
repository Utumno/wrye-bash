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

import locale as _locale
from functools import partial

import wx
from ._wx_locale_functions import GetLocaleInfoEx, LocaleNameToLCID

LC_ALL = _locale.LC_ALL

# language codes -> windows ? XXX
LANG_NEUTRAL = 0x00
LANG_INVARIANT = 0x7f
LANG_AFRIKAANS = 0x36
LANG_ALBANIAN = 0x1c
LANG_ALSATIAN = 0x84
LANG_AMHARIC = 0x5e
LANG_ARABIC = 0x01
LANG_ARMENIAN = 0x2b
LANG_ASSAMESE = 0x4d
LANG_AZERI = 0x2c
LANG_AZERBAIJANI = 0x2c
LANG_BANGLA = 0x45
LANG_BASHKIR = 0x6d
LANG_BASQUE = 0x2d
LANG_BELARUSIAN = 0x23
LANG_BENGALI = 0x45
LANG_BRETON = 0x7e
LANG_BOSNIAN = 0x1a
LANG_BOSNIAN_NEUTRAL = 0x781a
LANG_BULGARIAN = 0x02
LANG_CATALAN = 0x03
LANG_CENTRAL_KURDISH = 0x92
LANG_CHEROKEE = 0x5c
LANG_CHINESE = 0x04
LANG_CHINESE_SIMPLIFIED = 0x04
LANG_CHINESE_TRADITIONAL = 0x7c04
LANG_CORSICAN = 0x83
LANG_CROATIAN = 0x1a
LANG_CZECH = 0x05
LANG_DANISH = 0x06
LANG_DARI = 0x8c
LANG_DIVEHI = 0x65
LANG_DUTCH = 0x13
LANG_ENGLISH = 0x09
LANG_ESTONIAN = 0x25
LANG_FAEROESE = 0x38
LANG_FARSI = 0x29
LANG_FILIPINO = 0x64
LANG_FINNISH = 0x0b
LANG_FRENCH = 0x0c
LANG_FRISIAN = 0x62
LANG_FULAH = 0x67
LANG_GALICIAN = 0x56
LANG_GEORGIAN = 0x37
LANG_GERMAN = 0x07
LANG_GREEK = 0x08
LANG_GREENLANDIC = 0x6f
LANG_GUJARATI = 0x47
LANG_HAUSA = 0x68
LANG_HAWAIIAN = 0x75
LANG_HEBREW = 0x0d
LANG_HINDI = 0x39
LANG_HUNGARIAN = 0x0e
LANG_ICELANDIC = 0x0f
LANG_IGBO = 0x70
LANG_INDONESIAN = 0x21
LANG_INUKTITUT = 0x5d
LANG_IRISH = 0x3c
LANG_ITALIAN = 0x10
LANG_JAPANESE = 0x11
LANG_KANNADA = 0x4b
LANG_KASHMIRI = 0x60
LANG_KAZAK = 0x3f
LANG_KHMER = 0x53
LANG_KICHE = 0x86
LANG_KINYARWANDA = 0x87
LANG_KONKANI = 0x57
LANG_KOREAN = 0x12
LANG_KYRGYZ = 0x40
LANG_LAO = 0x54
LANG_LATVIAN = 0x26
LANG_LITHUANIAN = 0x27
LANG_LOWER_SORBIAN = 0x2e
LANG_LUXEMBOURGISH = 0x6e
LANG_MACEDONIAN = 0x2f
LANG_MALAY = 0x3e
LANG_MALAYALAM = 0x4c
LANG_MALTESE = 0x3a
LANG_MANIPURI = 0x58
LANG_MAORI = 0x81
LANG_MAPUDUNGUN = 0x7a
LANG_MARATHI = 0x4e
LANG_MOHAWK = 0x7c
LANG_MONGOLIAN = 0x50
LANG_NEPALI = 0x61
LANG_NORWEGIAN = 0x14
LANG_OCCITAN = 0x82
LANG_ODIA = 0x48
LANG_ORIYA = 0x48
LANG_PASHTO = 0x63
LANG_PERSIAN = 0x29
LANG_POLISH = 0x15
LANG_PORTUGUESE = 0x16
LANG_PULAR = 0x67
LANG_PUNJABI = 0x46
LANG_QUECHUA = 0x6b
LANG_ROMANIAN = 0x18
LANG_ROMANSH = 0x17
LANG_RUSSIAN = 0x19
LANG_SAKHA = 0x85
LANG_SAMI = 0x3b
LANG_SANSKRIT = 0x4f
LANG_SCOTTISH_GAELIC = 0x91
LANG_SERBIAN = 0x1a
LANG_SERBIAN_NEUTRAL = 0x7c1a
LANG_SINDHI = 0x59
LANG_SINHALESE = 0x5b
LANG_SLOVAK = 0x1b
LANG_SLOVENIAN = 0x24
LANG_SOTHO = 0x6c
LANG_SPANISH = 0x0a
LANG_SWAHILI = 0x41
LANG_SWEDISH = 0x1d
LANG_SYRIAC = 0x5a
LANG_TAJIK = 0x28
LANG_TAMAZIGHT = 0x5f
LANG_TAMIL = 0x49
LANG_TATAR = 0x44
LANG_TELUGU = 0x4a
LANG_THAI = 0x1e
LANG_TIBETAN = 0x51
LANG_TIGRIGNA = 0x73
LANG_TIGRINYA = 0x73
LANG_TSWANA = 0x32
LANG_TURKISH = 0x1f
LANG_TURKMEN = 0x42
LANG_UIGHUR = 0x80
LANG_UKRAINIAN = 0x22
LANG_UPPER_SORBIAN = 0x2e
LANG_URDU = 0x20
LANG_UZBEK = 0x43
LANG_VALENCIAN = 0x03
LANG_VIETNAMESE = 0x2a
LANG_WELSH = 0x52
LANG_WOLOF = 0x88
LANG_XHOSA = 0x34
LANG_YAKUT = 0x85
LANG_YI = 0x78
LANG_YORUBA = 0x6a
LANG_ZULU = 0x35

LANG_KABYLE = 0

SUBLANG_NEUTRAL = 0x00
SUBLANG_DEFAULT = 0x01
SUBLANG_SYS_DEFAULT = 0x02
SUBLANG_CUSTOM_DEFAULT = 0x03
SUBLANG_CUSTOM_UNSPECIFIED = 0x04
SUBLANG_UI_CUSTOM_DEFAULT = 0x05
SUBLANG_AFRIKAANS_SOUTH_AFRICA = 0x01
SUBLANG_ALBANIAN_ALBANIA = 0x01
SUBLANG_ALSATIAN_FRANCE = 0x01
SUBLANG_AMHARIC_ETHIOPIA = 0x01
SUBLANG_ARABIC_SAUDI_ARABIA = 0x01
SUBLANG_ARABIC_IRAQ = 0x02
SUBLANG_ARABIC_EGYPT = 0x03
SUBLANG_ARABIC_LIBYA = 0x04
SUBLANG_ARABIC_ALGERIA = 0x05
SUBLANG_ARABIC_MOROCCO = 0x06
SUBLANG_ARABIC_TUNISIA = 0x07
SUBLANG_ARABIC_OMAN = 0x08
SUBLANG_ARABIC_YEMEN = 0x09
SUBLANG_ARABIC_SYRIA = 0x0a
SUBLANG_ARABIC_JORDAN = 0x0b
SUBLANG_ARABIC_LEBANON = 0x0c
SUBLANG_ARABIC_KUWAIT = 0x0d
SUBLANG_ARABIC_UAE = 0x0e
SUBLANG_ARABIC_BAHRAIN = 0x0f
SUBLANG_ARABIC_QATAR = 0x10
SUBLANG_ARMENIAN_ARMENIA = 0x01
SUBLANG_ASSAMESE_INDIA = 0x01
SUBLANG_AZERI_LATIN = 0x01
SUBLANG_AZERI_CYRILLIC = 0x02
SUBLANG_AZERBAIJANI_AZERBAIJAN_LATIN = 0x01
SUBLANG_AZERBAIJANI_AZERBAIJAN_CYRILLIC = 0x02
SUBLANG_BANGLA_INDIA = 0x01
SUBLANG_BANGLA_BANGLADESH = 0x02
SUBLANG_BASHKIR_RUSSIA = 0x01
SUBLANG_BASQUE_BASQUE = 0x01
SUBLANG_BELARUSIAN_BELARUS = 0x01
SUBLANG_BENGALI_INDIA = 0x01
SUBLANG_BENGALI_BANGLADESH = 0x02
SUBLANG_BOSNIAN_BOSNIA_HERZEGOVINA_LATIN = 0x05
SUBLANG_BOSNIAN_BOSNIA_HERZEGOVINA_CYRILLIC = 0x08
SUBLANG_BRETON_FRANCE = 0x01
SUBLANG_BULGARIAN_BULGARIA = 0x01
SUBLANG_CATALAN_CATALAN = 0x01
SUBLANG_CENTRAL_KURDISH_IRAQ = 0x01
SUBLANG_CHEROKEE_CHEROKEE = 0x01
SUBLANG_CHINESE_TRADITIONAL = 0x01
SUBLANG_CHINESE_SIMPLIFIED = 0x02
SUBLANG_CHINESE_HONGKONG = 0x03
SUBLANG_CHINESE_SINGAPORE = 0x04
SUBLANG_CHINESE_MACAU = 0x05
SUBLANG_CORSICAN_FRANCE = 0x01
SUBLANG_CZECH_CZECH_REPUBLIC = 0x01
SUBLANG_CROATIAN_CROATIA = 0x01
SUBLANG_CROATIAN_BOSNIA_HERZEGOVINA_LATIN = 0x04
SUBLANG_DANISH_DENMARK = 0x01
SUBLANG_DARI_AFGHANISTAN = 0x01
SUBLANG_DIVEHI_MALDIVES = 0x01
SUBLANG_DUTCH = 0x01
SUBLANG_DUTCH_BELGIAN = 0x02
SUBLANG_ENGLISH_US = 0x01
SUBLANG_ENGLISH_UK = 0x02
SUBLANG_ENGLISH_AUS = 0x03
SUBLANG_ENGLISH_CAN = 0x04
SUBLANG_ENGLISH_NZ = 0x05
SUBLANG_ENGLISH_EIRE = 0x06
SUBLANG_ENGLISH_SOUTH_AFRICA = 0x07
SUBLANG_ENGLISH_JAMAICA = 0x08
SUBLANG_ENGLISH_CARIBBEAN = 0x09
SUBLANG_ENGLISH_BELIZE = 0x0a
SUBLANG_ENGLISH_TRINIDAD = 0x0b
SUBLANG_ENGLISH_ZIMBABWE = 0x0c
SUBLANG_ENGLISH_PHILIPPINES = 0x0d
SUBLANG_ENGLISH_INDIA = 0x10
SUBLANG_ENGLISH_MALAYSIA = 0x11
SUBLANG_ENGLISH_SINGAPORE = 0x12
SUBLANG_ESTONIAN_ESTONIA = 0x01
SUBLANG_FAEROESE_FAROE_ISLANDS = 0x01
SUBLANG_FILIPINO_PHILIPPINES = 0x01
SUBLANG_FINNISH_FINLAND = 0x01
SUBLANG_FRENCH = 0x01
SUBLANG_FRENCH_BELGIAN = 0x02
SUBLANG_FRENCH_CANADIAN = 0x03
SUBLANG_FRENCH_SWISS = 0x04
SUBLANG_FRENCH_LUXEMBOURG = 0x05
SUBLANG_FRENCH_MONACO = 0x06
SUBLANG_FRISIAN_NETHERLANDS = 0x01
SUBLANG_FULAH_SENEGAL = 0x02
SUBLANG_GALICIAN_GALICIAN = 0x01
SUBLANG_GEORGIAN_GEORGIA = 0x01
SUBLANG_GERMAN = 0x01
SUBLANG_GERMAN_SWISS = 0x02
SUBLANG_GERMAN_AUSTRIAN = 0x03
SUBLANG_GERMAN_LUXEMBOURG = 0x04
SUBLANG_GERMAN_LIECHTENSTEIN = 0x05
SUBLANG_GREEK_GREECE = 0x01
SUBLANG_GREENLANDIC_GREENLAND = 0x01
SUBLANG_GUJARATI_INDIA = 0x01
SUBLANG_HAUSA_NIGERIA_LATIN = 0x01
SUBLANG_HAWAIIAN_US = 0x01
SUBLANG_HEBREW_ISRAEL = 0x01
SUBLANG_HINDI_INDIA = 0x01
SUBLANG_HUNGARIAN_HUNGARY = 0x01
SUBLANG_ICELANDIC_ICELAND = 0x01
SUBLANG_IGBO_NIGERIA = 0x01
SUBLANG_INDONESIAN_INDONESIA = 0x01
SUBLANG_INUKTITUT_CANADA = 0x01
SUBLANG_INUKTITUT_CANADA_LATIN = 0x02
SUBLANG_IRISH_IRELAND = 0x02
SUBLANG_ITALIAN = 0x01
SUBLANG_ITALIAN_SWISS = 0x02
SUBLANG_JAPANESE_JAPAN = 0x01
SUBLANG_KANNADA_INDIA = 0x01
SUBLANG_KASHMIRI_SASIA = 0x02
SUBLANG_KASHMIRI_INDIA = 0x02
SUBLANG_KAZAK_KAZAKHSTAN = 0x01
SUBLANG_KHMER_CAMBODIA = 0x01
SUBLANG_KICHE_GUATEMALA = 0x01
SUBLANG_KINYARWANDA_RWANDA = 0x01
SUBLANG_KONKANI_INDIA = 0x01
SUBLANG_KOREAN = 0x01
SUBLANG_KYRGYZ_KYRGYZSTAN = 0x01
SUBLANG_LAO_LAO = 0x01
SUBLANG_LATVIAN_LATVIA = 0x01
SUBLANG_LITHUANIAN = 0x01
SUBLANG_LOWER_SORBIAN_GERMANY = 0x02
SUBLANG_LUXEMBOURGISH_LUXEMBOURG = 0x01
SUBLANG_MACEDONIAN_MACEDONIA = 0x01
SUBLANG_MALAY_MALAYSIA = 0x01
SUBLANG_MALAY_BRUNEI_DARUSSALAM = 0x02
SUBLANG_MALAYALAM_INDIA = 0x01
SUBLANG_MALTESE_MALTA = 0x01
SUBLANG_MAORI_NEW_ZEALAND = 0x01
SUBLANG_MAPUDUNGUN_CHILE = 0x01
SUBLANG_MARATHI_INDIA = 0x01
SUBLANG_MOHAWK_MOHAWK = 0x01
SUBLANG_MONGOLIAN_CYRILLIC_MONGOLIA = 0x01
SUBLANG_MONGOLIAN_PRC = 0x02
SUBLANG_NEPALI_INDIA = 0x02
SUBLANG_NEPALI_NEPAL = 0x01
SUBLANG_NORWEGIAN_BOKMAL = 0x01
SUBLANG_NORWEGIAN_NYNORSK = 0x02
SUBLANG_OCCITAN_FRANCE = 0x01
SUBLANG_ODIA_INDIA = 0x01
SUBLANG_ORIYA_INDIA = 0x01
SUBLANG_PASHTO_AFGHANISTAN = 0x01
SUBLANG_PERSIAN_IRAN = 0x01
SUBLANG_POLISH_POLAND = 0x01
SUBLANG_PORTUGUESE = 0x02
SUBLANG_PORTUGUESE_BRAZILIAN = 0x01
SUBLANG_PULAR_SENEGAL = 0x02
SUBLANG_PUNJABI_INDIA = 0x01
SUBLANG_PUNJABI_PAKISTAN = 0x02
SUBLANG_QUECHUA_BOLIVIA = 0x01
SUBLANG_QUECHUA_ECUADOR = 0x02
SUBLANG_QUECHUA_PERU = 0x03
SUBLANG_ROMANIAN_ROMANIA = 0x01
SUBLANG_ROMANSH_SWITZERLAND = 0x01
SUBLANG_RUSSIAN_RUSSIA = 0x01
SUBLANG_SAKHA_RUSSIA = 0x01
SUBLANG_SAMI_NORTHERN_NORWAY = 0x01
SUBLANG_SAMI_NORTHERN_SWEDEN = 0x02
SUBLANG_SAMI_NORTHERN_FINLAND = 0x03
SUBLANG_SAMI_LULE_NORWAY = 0x04
SUBLANG_SAMI_LULE_SWEDEN = 0x05
SUBLANG_SAMI_SOUTHERN_NORWAY = 0x06
SUBLANG_SAMI_SOUTHERN_SWEDEN = 0x07
SUBLANG_SAMI_SKOLT_FINLAND = 0x08
SUBLANG_SAMI_INARI_FINLAND = 0x09
SUBLANG_SANSKRIT_INDIA = 0x01
SUBLANG_SCOTTISH_GAELIC = 0x01
SUBLANG_SERBIAN_BOSNIA_HERZEGOVINA_LATIN = 0x06
SUBLANG_SERBIAN_BOSNIA_HERZEGOVINA_CYRILLIC = 0x07
SUBLANG_SERBIAN_MONTENEGRO_LATIN = 0x0b
SUBLANG_SERBIAN_MONTENEGRO_CYRILLIC = 0x0c
SUBLANG_SERBIAN_SERBIA_LATIN = 0x09
SUBLANG_SERBIAN_SERBIA_CYRILLIC = 0x0a
SUBLANG_SERBIAN_CROATIA = 0x01
SUBLANG_SERBIAN_LATIN = 0x02
SUBLANG_SERBIAN_CYRILLIC = 0x03
SUBLANG_SINDHI_INDIA = 0x01
SUBLANG_SINDHI_PAKISTAN = 0x02
SUBLANG_SINDHI_AFGHANISTAN = 0x02
SUBLANG_SINHALESE_SRI_LANKA = 0x01
SUBLANG_SOTHO_NORTHERN_SOUTH_AFRICA = 0x01
SUBLANG_SLOVAK_SLOVAKIA = 0x01
SUBLANG_SLOVENIAN_SLOVENIA = 0x01
SUBLANG_SPANISH = 0x01
SUBLANG_SPANISH_MEXICAN = 0x02
SUBLANG_SPANISH_MODERN = 0x03
SUBLANG_SPANISH_GUATEMALA = 0x04
SUBLANG_SPANISH_COSTA_RICA = 0x05
SUBLANG_SPANISH_PANAMA = 0x06
SUBLANG_SPANISH_DOMINICAN_REPUBLIC = 0x07
SUBLANG_SPANISH_VENEZUELA = 0x08
SUBLANG_SPANISH_COLOMBIA = 0x09
SUBLANG_SPANISH_PERU = 0x0a
SUBLANG_SPANISH_ARGENTINA = 0x0b
SUBLANG_SPANISH_ECUADOR = 0x0c
SUBLANG_SPANISH_CHILE = 0x0d
SUBLANG_SPANISH_URUGUAY = 0x0e
SUBLANG_SPANISH_PARAGUAY = 0x0f
SUBLANG_SPANISH_BOLIVIA = 0x10
SUBLANG_SPANISH_EL_SALVADOR = 0x11
SUBLANG_SPANISH_HONDURAS = 0x12
SUBLANG_SPANISH_NICARAGUA = 0x13
SUBLANG_SPANISH_PUERTO_RICO = 0x14
SUBLANG_SPANISH_US = 0x15
SUBLANG_SWAHILI_KENYA = 0x01
SUBLANG_SWEDISH = 0x01
SUBLANG_SWEDISH_FINLAND = 0x02
SUBLANG_SYRIAC_SYRIA = 0x01
SUBLANG_TAJIK_TAJIKISTAN = 0x01
SUBLANG_TAMAZIGHT_ALGERIA_LATIN = 0x02
SUBLANG_TAMAZIGHT_MOROCCO_TIFINAGH = 0x04
SUBLANG_TAMIL_INDIA = 0x01
SUBLANG_TAMIL_SRI_LANKA = 0x02
SUBLANG_TATAR_RUSSIA = 0x01
SUBLANG_TELUGU_INDIA = 0x01
SUBLANG_THAI_THAILAND = 0x01
SUBLANG_TIBETAN_PRC = 0x01
SUBLANG_TIGRIGNA_ERITREA = 0x02
SUBLANG_TIGRINYA_ERITREA = 0x02
SUBLANG_TIGRINYA_ETHIOPIA = 0x01
SUBLANG_TSWANA_BOTSWANA = 0x02
SUBLANG_TSWANA_SOUTH_AFRICA = 0x01
SUBLANG_TURKISH_TURKEY = 0x01
SUBLANG_TURKMEN_TURKMENISTAN = 0x01
SUBLANG_UIGHUR_PRC = 0x01
SUBLANG_UKRAINIAN_UKRAINE = 0x01
SUBLANG_UPPER_SORBIAN_GERMANY = 0x01
SUBLANG_URDU_PAKISTAN = 0x01
SUBLANG_URDU_INDIA = 0x02
SUBLANG_UZBEK_LATIN = 0x01
SUBLANG_UZBEK_CYRILLIC = 0x02
SUBLANG_VALENCIAN_VALENCIA = 0x02
SUBLANG_VIETNAMESE_VIETNAM = 0x01
SUBLANG_WELSH_UNITED_KINGDOM = 0x01
SUBLANG_WOLOF_SENEGAL = 0x01
SUBLANG_XHOSA_SOUTH_AFRICA = 0x01
SUBLANG_YAKUT_RUSSIA = 0x01
SUBLANG_YI_PRC = 0x01
SUBLANG_YORUBA_NIGERIA = 0x01
SUBLANG_ZULU_SOUTH_AFRICA = 0x01
SORT_DEFAULT = 0x0
SORT_INVARIANT_MATH = 0x1
SORT_JAPANESE_XJIS = 0x0
SORT_JAPANESE_UNICODE = 0x1
SORT_JAPANESE_RADICALSTROKE = 0x4
SORT_CHINESE_BIG5 = 0x0
SORT_CHINESE_PRCP = 0x0
SORT_CHINESE_UNICODE = 0x1
SORT_CHINESE_PRC = 0x2
SORT_CHINESE_BOPOMOFO = 0x3
SORT_CHINESE_RADICALSTROKE = 0x4
SORT_KOREAN_KSC = 0x0
SORT_KOREAN_UNICODE = 0x1
SORT_GERMAN_PHONE_BOOK = 0x1
SORT_HUNGARIAN_DEFAULT = 0x0
SORT_HUNGARIAN_TECHNICAL = 0x1
SORT_GEORGIAN_TRADITIONAL = 0x0
SORT_GEORGIAN_MODERN = 0x1

CODE_PAGES = {
    # IBM EBCDIC US-Canada
    37: 'IBM037',
    # OEM United States
    437: 'IBM437',
    # IBM EBCDIC International
    500: 'IBM500',
    # Arabic (ASMO 708)
    708: 'ASMO-708',
    # Arabic (ASMO-449+, BCON V4)
    709: 'ASMO-708',
    # Arabic (Transparent ASMO);
    # Arabic (DOS)
    720: 'DOS-720',
    # OEM Greek (formerly 437G);
    # Greek (DOS)
    737: 'ibm737',
    # OEM Baltic;
    # Baltic (DOS)
    775: 'ibm775',
    # OEM Multilingual Latin 1;
    # Western European (DOS)
    850: 'ibm850',
    # OEM Latin 2;
    # Central European (DOS)
    852: 'ibm852',
    # OEM Cyrillic (primarily Russian)
    855: 'IBM855',
    # OEM Turkish;
    # Turkish (DOS)
    857: 'ibm857',
    # OEM Multilingual Latin 1 + Euro symbol
    858: 'IBM00858',
    # OEM Portuguese;
    # Portuguese (DOS)
    860: 'IBM860',
    # OEM Icelandic;
    # Icelandic (DOS)
    861: 'ibm861',
    # OEM Hebrew;
    # Hebrew (DOS)
    862: 'DOS-862',
    # OEM French Canadian;
    #  French Canadian (DOS)
    863: 'IBM863',
    # OEM Arabic;
    # Arabic (864)
    864: 'IBM864',
    # OEM Nordic;
    # Nordic (DOS)
    865: 'IBM865',
    # OEM Russian;
    # Cyrillic (DOS)
    866: 'cp866',
    # OEM Modern Greek;
    # Greek, Modern (DOS)
    869: 'ibm869',
    # IBM EBCDIC Multilingual/ROECE (Latin 2);
    # IBM EBCDIC Multilingual Latin 2
    870: 'IBM870',
    # ANSI/OEM Thai (ISO 8859-11);
    # Thai (Windows)
    874: 'windows-874',
    # IBM EBCDIC Greek Modern
    875: 'cp875',
    # ANSI/OEM Japanese;
    # Japanese (Shift-JIS)
    932: 'shift_jis',
    # ANSI/OEM Simplified Chinese (PRC, Singapore);
    # Chinese Simplified (GB2312)
    936: 'gb2312',
    # ANSI/OEM Korean (Unified Hangul Code)
    949: 'ks_c_5601-1987',
    # ANSI/OEM Traditional Chinese (Taiwan; Hong Kong SAR, PRC);
    # Chinese Traditional (Big5)
    950: 'big5',
    # IBM EBCDIC Turkish (Latin 5)
    1026: 'IBM1026',
    # IBM EBCDIC Latin 1/Open System
    1047: 'IBM01047',
    # IBM EBCDIC US-Canada (037 + Euro symbol);
    # IBM EBCDIC (US-Canada-Euro)
    1140: 'IBM01140',
    # IBM EBCDIC Germany (20273 + Euro symbol);
    # IBM EBCDIC (Germany-Euro)
    1141: 'IBM01141',
    # IBM EBCDIC Denmark-Norway (20277 + Euro symbol);
    # IBM EBCDIC (Denmark-Norway-Euro)
    1142: 'IBM01142',
    # IBM EBCDIC Finland-Sweden (20278 + Euro symbol);
    # IBM EBCDIC (Finland-Sweden-Euro)
    1143: 'IBM01143',
    # IBM EBCDIC Italy (20280 + Euro symbol);
    # IBM EBCDIC (Italy-Euro)
    1144: 'IBM01144',
    # IBM EBCDIC Latin America-Spain (20284 + Euro symbol);
    # IBM EBCDIC (Spain-Euro)
    1145: 'IBM01145',
    # IBM EBCDIC United Kingdom (20285 + Euro symbol);
    # IBM EBCDIC (UK-Euro)
    1146: 'IBM01146',
    # IBM EBCDIC France (20297 + Euro symbol);
    # IBM EBCDIC (France-Euro)
    1147: 'IBM01147',
    # IBM EBCDIC International (500 + Euro symbol);
    # IBM EBCDIC (International-Euro)
    1148: 'IBM01148',
    # IBM EBCDIC Icelandic (20871 + Euro symbol);
    # IBM EBCDIC (Icelandic-Euro)
    1149: 'IBM01149',
    # Unicode UTF-16, little endian byte order (BMP of ISO 10646);
    # available only to managed applications
    1200: 'utf-16',
    # Unicode UTF-16, big endian byte order;
    # available only to managed applications
    1201: 'unicodeFFFE',
    # ANSI Central European;
    # Central European (Windows)
    1250: 'windows-1250',
    # ANSI Cyrillic;
    # Cyrillic (Windows)
    1251: 'windows-1251',
    # ANSI Latin 1;
    # Western European (Windows)
    1252: 'windows-1252',
    # ANSI Greek;
    # Greek (Windows)
    1253: 'windows-1253',
    # ANSI Turkish;
    # Turkish (Windows)
    1254: 'windows-1254',
    # ANSI Hebrew;
    # Hebrew (Windows)
    1255: 'windows-1255',
    # ANSI Arabic;
    # Arabic (Windows)
    1256: 'windows-1256',
    # ANSI Baltic;
    # Baltic (Windows)
    1257: 'windows-1257',
    # ANSI/OEM Vietnamese;
    # Vietnamese (Windows)
    1258: 'windows-1258',
    # Korean (Johab)
    1361: 'Johab',
    # MAC Roman; Western European (Mac)
    10000: 'macintosh',
    # Japanese (Mac)
    10001: 'x-mac-japanese',
    # MAC Traditional Chinese (Big5);
    # Chinese Traditional (Mac)
    10002: 'x-mac-chinesetrad',
    # Korean (Mac)
    10003: 'x-mac-korean',
    # Arabic (Mac)
    10004: 'x-mac-arabic',
    # Hebrew (Mac)
    10005: 'x-mac-hebrew',
    # Greek (Mac)
    10006: 'x-mac-greek',
    # Cyrillic (Mac)
    10007: 'x-mac-cyrillic',
    # MAC Simplified Chinese (GB 2312);
    # Chinese Simplified (Mac)
    10008: 'x-mac-chinesesimp',
    # Romanian (Mac)
    10010: 'x-mac-romanian',
    # Ukrainian (Mac)
    10017: 'x-mac-ukrainian',
    # Thai (Mac)
    10021: 'x-mac-thai',
    # MAC Latin 2;
    # Central European (Mac)
    10029: 'x-mac-ce',
    # Icelandic (Mac)
    10079: 'x-mac-icelandic',
    # Turkish (Mac)
    10081: 'x-mac-turkish',
    # Croatian (Mac)
    10082: 'x-mac-croatian',
    # Unicode UTF-32, little endian byte order;
    # available only to managed applications
    12000: 'utf-32',
    # Unicode UTF-32, big endian byte order;
    # available only to managed applications
    12001: 'utf-32BE',
    # CNS Taiwan;
    # Chinese Traditional (CNS)
    20000: 'x-Chinese_CNS',
    # TCA Taiwan
    20001: 'x-cp20001',
    # Eten Taiwan;
    # Chinese Traditional (Eten)
    20002: 'x_Chinese-Eten',
    # IBM5550 Taiwan
    20003: 'x-cp20003',
    # TeleText Taiwan
    20004: 'x-cp20004',
    # Wang Taiwan
    20005: 'x-cp20005',
    # IA5 (IRV International Alphabet No. 5, 7-bit);
    # Western European (IA5)
    20105: 'x-IA5',
    # IA5 German (7-bit)
    20106: 'x-IA5-German',
    # IA5 Swedish (7-bit)
    20107: 'x-IA5-Swedish',
    # IA5 Norwegian (7-bit)
    20108: 'x-IA5-Norwegian',
    # US-ASCII (7-bit)
    20127: 'us-ascii',
    # T.61
    20261: 'x-cp20261',
    # ISO 6937 Non-Spacing Accent
    20269: 'x-cp20269',
    # IBM EBCDIC Germany
    20273: 'IBM273',
    # IBM EBCDIC Denmark-Norway
    20277: 'IBM277',
    # IBM EBCDIC Finland-Sweden
    20278: 'IBM278',
    # IBM EBCDIC Italy
    20280: 'IBM280',
    # IBM EBCDIC Latin America-Spain
    20284: 'IBM284',
    # IBM EBCDIC United Kingdom
    20285: 'IBM285',
    # IBM EBCDIC Japanese Katakana Extended
    20290: 'IBM290',
    # IBM EBCDIC France
    20297: 'IBM297',
    # IBM EBCDIC Arabic
    20420: 'IBM420',
    # IBM EBCDIC Greek
    20423: 'IBM423',
    # IBM EBCDIC Hebrew
    20424: 'IBM424',
    # IBM EBCDIC Korean Extended
    20833: 'x-EBCDIC-KoreanExtended',
    # IBM EBCDIC Thai
    20838: 'IBM-Thai',
    # Russian (KOI8-R);
    # Cyrillic (KOI8-R)
    20866: 'koi8-r',
    # IBM EBCDIC Icelandic
    20871: 'IBM871',
    # IBM EBCDIC Cyrillic Russian
    20880: 'IBM880',
    # IBM EBCDIC Turkish
    20905: 'IBM905',
    # IBM EBCDIC Latin 1/Open System (1047 + Euro symbol)
    20924: 'IBM00924',
    # Japanese (JIS 0208-1990 and 0212-1990)
    20932: 'EUC-JP',
    # Simplified Chinese (GB2312);
    # Chinese Simplified (GB2312-80)
    20936: 'x-cp20936',
    # Korean Wansung
    20949: 'x-cp20949',
    # IBM EBCDIC Cyrillic Serbian-Bulgarian
    21025: 'cp1025',
    # Ukrainian (KOI8-U);
    # Cyrillic (KOI8-U)
    21866: 'koi8-u',
    # ISO 8859-1 Latin 1;
    # Western European (ISO)
    28591: 'iso-8859-1',
    # ISO 8859-2 Central European;
    # Central European (ISO)
    28592: 'iso-8859-2',
    # ISO 8859-3 Latin 3
    28593: 'iso-8859-3',
    # ISO 8859-4 Baltic
    28594: 'iso-8859-4',
    # ISO 8859-5 Cyrillic
    28595: 'iso-8859-5',
    # ISO 8859-6 Arabic
    28596: 'iso-8859-6',
    # ISO 8859-7 Greek
    28597: 'iso-8859-7',
    # ISO 8859-8 Hebrew;
    # Hebrew (ISO-Visual)
    28598: 'iso-8859-8',
    # ISO 8859-9 Turkish
    28599: 'iso-8859-9',
    # ISO 8859-13 Estonian
    28603: 'iso-8859-13',
    # ISO 8859-15 Latin 9
    28605: 'iso-8859-15',
    # Europa 3
    29001: 'x-Europa',
    # ISO 8859-8 Hebrew;
    # Hebrew (ISO-Logical)
    38598: 'iso-8859-8-i',
    # ISO 2022 Japanese with no halfwidth Katakana;
    # Japanese (JIS)
    50220: 'iso-2022-jp',
    # ISO 2022 Japanese with halfwidth Katakana;
    # Japanese (JIS-Allow 1 byte Kana)
    50221: 'csISO2022JP',
    # ISO 2022 Japanese JIS X 0201-1989;
    # Japanese (JIS-Allow 1 byte Kana - SO/SI)
    50222: 'iso-2022-jp',
    # ISO 2022 Korean
    50225: 'iso-2022-kr',
    # ISO 2022 Simplified Chinese;
    # Chinese Simplified (ISO 2022)
    50227: 'x-cp50227',
    # EUC Japanese
    51932: 'euc-jp',
    # EUC Simplified Chinese;
    # Chinese Simplified (EUC)
    51936: 'EUC-CN',
    # EUC Korean
    51949: 'euc-kr',
    # HZ-GB2312 Simplified Chinese;
    # Chinese Simplified (HZ)
    52936: 'hz-gb-2312',
    # Windows XP and later:
    # GB18030 Simplified Chinese (4 byte);
    # Chinese Simplified (GB18030)
    54936: 'GB18030',
    # ISCII Devanagari
    57002: 'x-iscii-de',
    # ISCII Bangla
    57003: 'x-iscii-be',
    # ISCII Tamil
    57004: 'x-iscii-ta',
    # ISCII Telugu
    57005: 'x-iscii-te',
    # ISCII Assamese
    57006: 'x-iscii-as',
    # ISCII Odia
    57007: 'x-iscii-or',
    # ISCII Kannada
    57008: 'x-iscii-ka',
    # ISCII Malayalam
    57009: 'x-iscii-ma',
    # ISCII Gujarati
    57010: 'x-iscii-gu',
    # ISCII Punjabi
    57011: 'x-iscii-pa',
    # Unicode (UTF-7)
    65000: 'utf-7',
    # Unicode (UTF-8)
    65001: 'utf-8'
}


LOCALE_NAME_MAX_LENGTH = 85
LOCALE_ALLOW_NEUTRAL_NAMES = 0x08000000
LOCALE_SENGLISHLANGUAGENAME = 0x00001001
LOCALE_SENGLISHCOUNTRYNAME = 0x00001002
LOCALE_IDEFAULTANSICODEPAGE = 0x00001004
LOCALE_SNATIVELANGUAGENAME = 0x00000004
LOCALE_SLOCALIZEDLANGUAGENAME = 0x0000006f
LOCALE_SNATIVECOUNTRYNAME = 0x00000008
LOCALE_SLOCALIZEDCOUNTRYNAME = 0x00000006


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

def LNGINFO(wxlang, canonical, winlang, winsublang, layout, desc, locale_class):
    """LanguageInfo factory - adds to locale \"db\""""
    info = LanguageInfo()
    info.Language = wxlang
    info.CanonicalName = canonical
    info.LayoutDirection = layout
    info.Description = desc
    # extra attributes of LanguageInfo vs wx.LanguageInfo
    info.WinLang = winlang,
    info.WinSublang = winsublang
    locale_class.AddLanguage(info)
    return info

def _add_languages_to_db(locale_class):
    LNG = partial(LNGINFO, locale_class=locale_class)
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
