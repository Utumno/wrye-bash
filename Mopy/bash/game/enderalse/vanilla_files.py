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
"""This module lists the files installed in the Data folder in a completely
vanilla Enderal SE setup."""

# Entries for other languages manually added from SteamDB:
# https://steamdb.info/app/976620/depots/
vanilla_files = {
    'Enderal - Forgotten Stories.ini',
    'Interface\\00E_heromenu.swf',
    'Interface\\1.5.9.0patchnote and Japanes localization updates.txt',
    'Interface\\controls\\pc\\controlmap.txt',
    'Interface\\credits.txt',
    'Interface\\credits_plru.txt',
    'Interface\\dialoguemenu.swf',
    'Interface\\Enderal_jpfp.swf',
    'Interface\\Enderal_jpfp_console.swf',
    'Interface\\Enderal_jpfp_Handwritten.swf',
    'Interface\\Enderal_jpfp_Menu.swf',
    'Interface\\exported\\hudmenu.gfx',
    'Interface\\exported\\widgets\\skyui\\followerpanel.swf',
    'Interface\\FangZhengKaiTi_GBK.swf',
    'Interface\\fontconfig.txt',
    'Interface\\fonts_en2.swf',
    'Interface\\Japanese_Credits.txt',
    'Interface\\quest_journal.swf',
    'Interface\\skyui\\icons_category_psychosteve.swf',
    'Interface\\startmenu.swf',
    'Interface\\statssheetmenu.swf',
    'Interface\\translate_english.txt',
    'Interface\\translate_chinese.txt',
    'Interface\\translate_german.txt',
    'Interface\\translate_italian.txt',
    'Interface\\translate_japanese.txt',
    'Interface\\translate_korean.txt',
    'Interface\\translate_russian.txt',
    'Interface\\translate_spanish.txt',
    'Interface\\translations\\buriedtreasure_chinese.txt',
    'Interface\\translations\\buriedtreasure_french.txt',
    'Interface\\translations\\buriedtreasure_italian.txt',
    'Interface\\translations\\buriedtreasure_japanese.txt',
    'Interface\\translations\\buriedtreasure_korean.txt',
    'Interface\\translations\\skyui_se_chinese.txt',
    'Interface\\translations\\skyui_se_japanese.txt',
    'Interface\\translations\\skyui_se_korean.txt',
    'Interface\\translations\\taverngames_chinese.txt',
    'Interface\\translations\\taverngames_french.txt',
    'Interface\\translations\\taverngames_german.txt',
    'Interface\\translations\\taverngames_italian.txt',
    'Interface\\translations\\taverngames_japanese.txt',
    'Interface\\translations\\taverngames_russian.txt',
    'Interface\\translations\\taverngames_spanish.txt',
    'Interface\\translations\\uiextensions_chinese.txt',
    'Interface\\translations\\uiextensions_french.txt',
    'Interface\\translations\\uiextensions_german.txt',
    'Interface\\translations\\uiextensions_italian.txt',
    'Interface\\translations\\uiextensions_japanese.txt',
    'Interface\\translations\\uiextensions_korean.txt',
    'meshes\\actors\\character\\behaviors\\0_master.hkx',
    'meshes\\actors\\character\\behaviors\\1hm_behavior.hkx',
    'meshes\\actors\\character\\behaviors\\FNIS_Enderal_Behavior.hkx',
    'meshes\\actors\\character\\behaviors\\FNIS_FNISBase_Behavior.hkx',
    'meshes\\actors\\character\\behaviors\\FNIS_PaleTest04_Behavior.hkx',
    'meshes\\actors\\character\\behaviors\\FNIS_PipeSmoking_Behavior.hkx',
    'meshes\\actors\\character\\behaviors\\idlebehavior.hkx',
    'meshes\\actors\\character\\behaviors\\mt_behavior.hkx',
    'meshes\\actors\\character\\behaviors\\sprintbehavior.hkx',
    'meshes\\actors\\character\\character assets\\skeleton.hkx',
    'meshes\\actors\\character\\character assets\\skeleton.nif',
    'meshes\\actors\\character\\character assets\\skeleton.xml',
    'meshes\\actors\\character\\character assets\\skeletonbeast.nif',
    'meshes\\actors\\character\\character assets female\\skeletonbeast_female.nif',
    'meshes\\actors\\character\\character assets female\\skeleton_female.hkx',
    'meshes\\actors\\character\\character assets female\\skeleton_female.nif',
    'meshes\\actors\\character\\character assets female\\skeleton_female.xml',
    'meshes\\actors\\character\\characters\\defaultmale.hkx',
    'meshes\\actors\\character\\characters female\\defaultfemale.hkx',
    'meshes\\actors\\character\\_1stperson\\skeleton.nif',
    'meshes\\animationdatasinglefile.txt',
    'meshes\\animationsetdatasinglefile.txt',
    'meshes\\terrain\\Vyn\\vyn.32.-5.9.btr',
    'Scripts\\ActiveMagicEffect.pex',
    'Scripts\\Actor.pex',
    'Scripts\\ActorBase.pex',
    'Scripts\\ActorValueInfo.pex',
    'Scripts\\Alias.pex',
    'Scripts\\Ammo.pex',
    'Scripts\\Apparatus.pex',
    'Scripts\\Armor.pex',
    'Scripts\\ArmorAddon.pex',
    'Scripts\\Art.pex',
    'Scripts\\Book.pex',
    'Scripts\\Camera.pex',
    'Scripts\\Cell.pex',
    'Scripts\\ColorComponent.pex',
    'Scripts\\ColorForm.pex',
    'Scripts\\CombatStyle.pex',
    'Scripts\\ConstructibleObject.pex',
    'Scripts\\DefaultObjectManager.pex',
    'Scripts\\Enchantment.pex',
    'Scripts\\EquipSlot.pex',
    'Scripts\\Faction.pex',
    'Scripts\\Flora.pex',
    'Scripts\\Form.pex',
    'Scripts\\FormList.pex',
    'Scripts\\FormType.pex',
    'Scripts\\Game.pex',
    'Scripts\\GameData.pex',
    'Scripts\\HeadPart.pex',
    'Scripts\\Ingredient.pex',
    'Scripts\\Input.pex',
    'Scripts\\JArray.pex',
    'Scripts\\JAtomic.pex',
    'Scripts\\JContainers.pex',
    'Scripts\\JContainers_DomainExample.pex',
    'Scripts\\JDB.pex',
    'Scripts\\JFormDB.pex',
    'Scripts\\JFormMap.pex',
    'Scripts\\JIntMap.pex',
    'Scripts\\JLua.pex',
    'Scripts\\JMap.pex',
    'Scripts\\JString.pex',
    'Scripts\\JValue.pex',
    'Scripts\\Keyword.pex',
    'Scripts\\LeveledActor.pex',
    'Scripts\\LeveledItem.pex',
    'Scripts\\LeveledSpell.pex',
    'Scripts\\Location.pex',
    'Scripts\\MagicEffect.pex',
    'Scripts\\Math.pex',
    'Scripts\\ModEvent.pex',
    'Scripts\\NetImmerse.pex',
    'Scripts\\objectreference.pex',
    'Scripts\\Outfit.pex',
    'Scripts\\Perk.pex',
    'Scripts\\potion.pex',
    'Scripts\\Quest.pex',
    'Scripts\\Race.pex',
    'Scripts\\Scroll.pex',
    'Scripts\\Shout.pex',
    'Scripts\\ski_favoritesmanager.pex',
    'Scripts\\SKSE.pex',
    'Scripts\\SoulGem.pex',
    'Scripts\\Sound.pex',
    'Scripts\\SoundDescriptor.pex',
    'Scripts\\Source\\ActiveMagicEffect.psc',
    'Scripts\\Source\\Actor.psc',
    'Scripts\\Source\\ActorBase.psc',
    'Scripts\\Source\\ActorValueInfo.psc',
    'Scripts\\Source\\Alias.psc',
    'Scripts\\Source\\Ammo.psc',
    'Scripts\\Source\\Apparatus.psc',
    'Scripts\\Source\\Armor.psc',
    'Scripts\\Source\\ArmorAddon.psc',
    'Scripts\\Source\\Art.psc',
    'Scripts\\Source\\Book.psc',
    'Scripts\\Source\\Camera.psc',
    'Scripts\\Source\\Cell.psc',
    'Scripts\\Source\\ColorComponent.psc',
    'Scripts\\Source\\ColorForm.psc',
    'Scripts\\Source\\CombatStyle.psc',
    'Scripts\\Source\\ConstructibleObject.psc',
    'Scripts\\Source\\DefaultObjectManager.psc',
    'Scripts\\Source\\Enchantment.psc',
    'Scripts\\Source\\EquipSlot.psc',
    'Scripts\\Source\\Faction.psc',
    'Scripts\\Source\\Flora.psc',
    'Scripts\\Source\\Form.psc',
    'Scripts\\Source\\FormList.psc',
    'Scripts\\Source\\FormType.psc',
    'Scripts\\Source\\Game.psc',
    'Scripts\\Source\\GameData.psc',
    'Scripts\\Source\\HeadPart.psc',
    'Scripts\\Source\\Ingredient.psc',
    'Scripts\\Source\\Input.psc',
    'Scripts\\Source\\JArray.psc',
    'Scripts\\Source\\JAtomic.psc',
    'Scripts\\Source\\JContainers.psc',
    'Scripts\\Source\\JContainers_DomainExample.psc',
    'Scripts\\Source\\JDB.psc',
    'Scripts\\Source\\JFormDB.psc',
    'Scripts\\Source\\JFormMap.psc',
    'Scripts\\Source\\JIntMap.psc',
    'Scripts\\Source\\JLua.psc',
    'Scripts\\Source\\JMap.psc',
    'Scripts\\Source\\JString.psc',
    'Scripts\\Source\\JValue.psc',
    'Scripts\\Source\\Keyword.psc',
    'Scripts\\Source\\LeveledActor.psc',
    'Scripts\\Source\\LeveledItem.psc',
    'Scripts\\Source\\LeveledSpell.psc',
    'Scripts\\Source\\Location.psc',
    'Scripts\\Source\\MagicEffect.psc',
    'Scripts\\Source\\Math.psc',
    'Scripts\\Source\\ModEvent.psc',
    'Scripts\\Source\\NetImmerse.psc',
    'Scripts\\Source\\ObjectReference.psc',
    'Scripts\\Source\\Outfit.psc',
    'Scripts\\Source\\Perk.psc',
    'Scripts\\Source\\Potion.psc',
    'Scripts\\Source\\Quest.psc',
    'Scripts\\Source\\Race.psc',
    'Scripts\\Source\\Scroll.psc',
    'Scripts\\Source\\Shout.psc',
    'Scripts\\Source\\ski_favoritesmanager.psc',
    'Scripts\\Source\\SKSE.psc',
    'Scripts\\Source\\SoulGem.psc',
    'Scripts\\Source\\Sound.psc',
    'Scripts\\Source\\SoundDescriptor.psc',
    'Scripts\\Source\\SpawnerTask.psc',
    'Scripts\\Source\\Spell.psc',
    'Scripts\\Source\\StringUtil.psc',
    'Scripts\\Source\\TextureSet.psc',
    'Scripts\\Source\\TreeObject.psc',
    'Scripts\\Source\\UI.psc',
    'Scripts\\Source\\UICallback.psc',
    'Scripts\\Source\\Utility.psc',
    'Scripts\\Source\\Weapon.psc',
    'Scripts\\Source\\Weather.psc',
    'Scripts\\Source\\WornObject.psc',
    'Scripts\\SpawnerTask.pex',
    'Scripts\\Spell.pex',
    'Scripts\\StringUtil.pex',
    'Scripts\\TextureSet.pex',
    'Scripts\\TreeObject.pex',
    'Scripts\\UI.pex',
    'Scripts\\UICallback.pex',
    'Scripts\\Utility.pex',
    'Scripts\\Weapon.pex',
    'Scripts\\Weather.pex',
    'Scripts\\WornObject.pex',
    'SKSE\\Plugins\\EngineFixes.dll',
    'SKSE\\Plugins\\EngineFixes.toml',
    'SKSE\\Plugins\\EngineFixes_preload.txt',
    'SKSE\\Plugins\\EngineFixes_SNCT.toml',
    'SKSE\\Plugins\\FlatMapMarkersSSE.dll',
    'SKSE\\Plugins\\FlatMapMarkersSSE.json',
    'SKSE\\Plugins\\fs.dll',
    'SKSE\\Plugins\\fs_src.7z',
    'SKSE\\Plugins\\fs_steam.dll',
    'SKSE\\Plugins\\JCData\\Domains\\.force-install',
    'SKSE\\Plugins\\JCData\\InternalLuaScripts\\api_for_lua.h',
    'SKSE\\Plugins\\JCData\\InternalLuaScripts\\init.lua',
    'SKSE\\Plugins\\JCData\\InternalLuaScripts\\jc.lua',
    'SKSE\\Plugins\\JCData\\lua\\jc\\init.lua',
    'SKSE\\Plugins\\JCData\\lua\\testing\\basic.lua',
    'SKSE\\Plugins\\JCData\\lua\\testing\\init.lua',
    'SKSE\\Plugins\\JCData\\lua\\testing\\jc-tests.lua',
    'SKSE\\Plugins\\JCData\\lua\\testing\\misc.lua',
    'SKSE\\Plugins\\JCData\\lua\\testing\\test.lua',
    'SKSE\\Plugins\\JContainers64.dll',
    'SKSE\\Plugins\\SkyrimRedirector.dll',
    'SKSE\\Plugins\\SkyrimRedirector.ini',
    'SKSE\\Plugins\\SkyrimRedirector.log',
    'SKSE\\Plugins\\SSEDisplayTweaks.dll',
    'SKSE\\Plugins\\SSEDisplayTweaks.ini',
    'SKSE\\Plugins\\version-1-5-16-0.bin',
    'SKSE\\Plugins\\version-1-5-23-0.bin',
    'SKSE\\Plugins\\version-1-5-3-0.bin',
    'SKSE\\Plugins\\version-1-5-39-0.bin',
    'SKSE\\Plugins\\version-1-5-50-0.bin',
    'SKSE\\Plugins\\version-1-5-53-0.bin',
    'SKSE\\Plugins\\version-1-5-62-0.bin',
    'SKSE\\Plugins\\version-1-5-73-0.bin',
    'SKSE\\Plugins\\version-1-5-80-0.bin',
    'SKSE\\Plugins\\version-1-5-97-0.bin',
    'SKSE\\Plugins\\YesImSure.dll',
    'SKSE\\Plugins\\YesImSure.json',
    'SKSE\\SKSE.ini',
    'SkyUI_SE.ini',
    'Strings\\enderal - forgotten stories_chinese.dlstrings',
    'Strings\\enderal - forgotten stories_chinese.ilstrings',
    'Strings\\enderal - forgotten stories_chinese.strings',
    'Strings\\enderal - forgotten stories_english.dlstrings',
    'Strings\\enderal - forgotten stories_english.ilstrings',
    'Strings\\enderal - forgotten stories_english.strings',
    'Strings\\enderal - forgotten stories_french.dlstrings',
    'Strings\\enderal - forgotten stories_french.ilstrings',
    'Strings\\enderal - forgotten stories_french.strings',
    'Strings\\enderal - forgotten stories_german.dlstrings',
    'Strings\\enderal - forgotten stories_german.ilstrings',
    'Strings\\enderal - forgotten stories_german.strings',
    'Strings\\enderal - forgotten stories_italian.dlstrings',
    'Strings\\enderal - forgotten stories_italian.ilstrings',
    'Strings\\enderal - forgotten stories_italian.strings',
    'Strings\\enderal - forgotten stories_japanese.dlstrings',
    'Strings\\enderal - forgotten stories_japanese.ilstrings',
    'Strings\\enderal - forgotten stories_japanese.strings',
    'Strings\\enderal - forgotten stories_korean.dlstrings',
    'Strings\\enderal - forgotten stories_korean.ilstrings',
    'Strings\\enderal - forgotten stories_korean.strings',
    'Strings\\enderal - forgotten stories_russian.dlstrings',
    'Strings\\enderal - forgotten stories_russian.ilstrings',
    'Strings\\enderal - forgotten stories_russian.strings',
    'Strings\\enderal - forgotten stories_spanish.dlstrings',
    'Strings\\enderal - forgotten stories_spanish.ilstrings',
    'Strings\\enderal - forgotten stories_spanish.strings',
    'Strings\\skyrim_chinese.dlstrings',
    'Strings\\skyrim_chinese.ilstrings',
    'Strings\\skyrim_chinese.strings',
    'Strings\\skyrim_english.dlstrings',
    'Strings\\skyrim_english.ilstrings',
    'Strings\\skyrim_english.strings',
    'Strings\\skyrim_french.dlstrings',
    'Strings\\skyrim_french.ilstrings',
    'Strings\\skyrim_french.strings',
    'Strings\\skyrim_german.dlstrings',
    'Strings\\skyrim_german.ilstrings',
    'Strings\\skyrim_german.strings',
    'Strings\\skyrim_italian.dlstrings',
    'Strings\\skyrim_italian.ilstrings',
    'Strings\\skyrim_italian.strings',
    'Strings\\skyrim_japanese.dlstrings',
    'Strings\\skyrim_japanese.ilstrings',
    'Strings\\skyrim_japanese.strings',
    'Strings\\skyrim_korean.dlstrings',
    'Strings\\skyrim_korean.ilstrings',
    'Strings\\skyrim_korean.strings',
    'Strings\\skyrim_russian.dlstrings',
    'Strings\\skyrim_russian.ilstrings',
    'Strings\\skyrim_russian.strings',
    'Strings\\skyrim_spanish.dlstrings',
    'Strings\\skyrim_spanish.ilstrings',
    'Strings\\skyrim_spanish.strings',
    'Video\\EnderalIntro.bik',
    'Video\\Enderal_Credits.bik',
    'Video\\MQ17BlackGuardian.bik',
    'Video\\MQP03NearDeathExperience.bik',
    '_Enderal - Forgotten Stories.ini',
}
