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
#  Wrye Bash copyright (C) 2005-2009 Wrye, 2010-2022 Wrye Bash Team
#  https://github.com/wrye-bash
#
# =============================================================================

"""This package contains the Skyrim specific patchers. This module
contains the data structures that are dynamically set on a per game basis in
bush."""
# ***no imports!***

# Function Info ---------------------------------------------------------------
# 0: no param; 1: int param; 2: formid param; 3: float param
# Third parameter is always sint32, so no need to specify here
condition_function_data = {
    0:    (u'GetWantBlocking', 0, 0),
    1:    (u'GetDistance', 2, 0),
    5:    (u'GetLocked', 0, 0),
    6:    (u'GetPos', 0, 0),
    8:    (u'GetAngle', 0, 0),
    10:   (u'GetStartingPos', 0, 0),
    11:   (u'GetStartingAngle', 0, 0),
    12:   (u'GetSecondsPassed', 0, 0),
    14:   (u'GetActorValue', 2, 0),
    18:   (u'GetCurrentTime', 0, 0),
    24:   (u'GetScale', 0, 0),
    25:   (u'IsMoving', 0, 0),
    26:   (u'IsTurning', 0, 0),
    27:   (u'GetLineOfSight', 2, 0),
    32:   (u'GetInSameCell', 2, 0),
    35:   (u'GetDisabled', 0, 0),
    36:   (u'MenuMode', 1, 0),
    39:   (u'GetDisease', 0, 0),
    41:   (u'GetClothingValue', 0, 0),
    42:   (u'SameFaction', 2, 0),
    43:   (u'SameRace', 2, 0),
    44:   (u'SameSex', 2, 0),
    45:   (u'GetDetected', 2, 0),
    46:   (u'GetDead', 0, 0),
    47:   (u'GetItemCount', 2, 0),
    48:   (u'GetGold', 0, 0),
    49:   (u'GetSleeping', 0, 0),
    50:   (u'GetTalkedToPC', 0, 0),
    53:   (u'GetScriptVariable', 2, 0),
    56:   (u'GetQuestRunning', 2, 0),
    58:   (u'GetStage', 2, 0),
    59:   (u'GetStageDone', 2, 1),
    60:   (u'GetFactionRankDifference', 2, 2),
    61:   (u'GetAlarmed', 0, 0),
    62:   (u'IsRaining', 0, 0),
    63:   (u'GetAttacked', 0, 0),
    64:   (u'GetIsCreature', 0, 0),
    65:   (u'GetLockLevel', 0, 0),
    66:   (u'GetShouldAttack', 2, 0),
    67:   (u'GetInCell', 2, 0),
    68:   (u'GetIsClass', 2, 0),
    69:   (u'GetIsRace', 2, 0),
    70:   (u'GetIsSex', 1, 0),
    71:   (u'GetInFaction', 2, 0),
    72:   (u'GetIsID', 2, 0),
    73:   (u'GetFactionRank', 2, 0),
    74:   (u'GetGlobalValue', 2, 0),
    75:   (u'IsSnowing', 0, 0),
    77:   (u'GetRandomPercent', 0, 0),
    79:   (u'GetQuestVariable', 2, 0),
    80:   (u'GetLevel', 0, 0),
    81:   (u'IsRotating', 0, 0),
    84:   (u'GetDeadCount', 2, 0),
    91:   (u'GetIsAlerted', 0, 0),
    98:   (u'GetPlayerControlsDisabled', 1, 1),
    99:   (u'GetHeadingAngle', 2, 0),
    101:  (u'IsWeaponMagicOut', 0, 0),
    102:  (u'IsTorchOut', 0, 0),
    103:  (u'IsShieldOut', 0, 0),
    106:  (u'IsFacingUp', 0, 0),
    107:  (u'GetKnockedState', 0, 0),
    108:  (u'GetWeaponAnimType', 0, 0),
    109:  (u'IsWeaponSkillType', 2, 0),
    110:  (u'GetCurrentAIPackage', 0, 0),
    111:  (u'IsWaiting', 0, 0),
    112:  (u'IsIdlePlaying', 0, 0),
    116:  (u'IsIntimidatedbyPlayer', 0, 0),
    117:  (u'IsPlayerInRegion', 0, 0),
    118:  (u'GetActorAggroRadiusViolated', 0, 0),
    122:  (u'GetCrime', 2, 1),
    123:  (u'IsGreetingPlayer', 0, 0),
    125:  (u'IsGuard', 0, 0),
    127:  (u'HasBeenEaten', 0, 0),
    128:  (u'GetStaminaPercentage', 0, 0),
    129:  (u'GetPCIsClass', 2, 0),
    130:  (u'GetPCIsRace', 2, 0),
    131:  (u'GetPCIsSex', 1, 0),
    132:  (u'GetPCInFaction', 2, 0),
    133:  (u'SameFactionAsPC', 0, 0),
    134:  (u'SameRaceAsPC', 0, 0),
    135:  (u'SameSexAsPC', 0, 0),
    136:  (u'GetIsReference', 2, 0),
    141:  (u'IsTalking', 0, 0),
    142:  (u'GetWalkSpeed', 0, 0),
    143:  (u'GetCurrentAIProcedure', 0, 0),
    144:  (u'GetTrespassWarningLevel', 0, 0),
    145:  (u'IsTrespassing', 0, 0),
    146:  (u'IsInMyOwnedCell', 0, 0),
    147:  (u'GetWindSpeed', 0, 0),
    148:  (u'GetCurrentWeatherPercent', 0, 0),
    149:  (u'GetIsCurrentWeather', 2, 0),
    150:  (u'IsContinuingPackagePCNear', 0, 0),
    152:  (u'GetIsCrimeFaction', 2, 0),
    153:  (u'CanHaveFlames', 0, 0),
    154:  (u'HasFlames', 0, 0),
    157:  (u'GetOpenState', 0, 0),
    159:  (u'GetSitting', 0, 0),
    161:  (u'GetIsCurrentPackage', 2, 0),
    162:  (u'IsCurrentFurnitureRef', 2, 0),
    163:  (u'IsCurrentFurnitureObj', 2, 0),
    170:  (u'GetDayOfWeek', 0, 0),
    172:  (u'GetTalkedToPCParam', 2, 0),
    175:  (u'IsPCSleeping', 0, 0),
    176:  (u'IsPCAMurderer', 0, 0),
    180:  (u'HasSameEditorLocAsRef', 2, 2),
    181:  (u'HasSameEditorLocAsRefAlias', 1, 2),
    182:  (u'GetEquipped', 2, 0),
    185:  (u'IsSwimming', 0, 0),
    190:  (u'GetAmountSoldStolen', 0, 0),
    192:  (u'GetIgnoreCrime', 0, 0),
    193:  (u'GetPCExpelled', 2, 0),
    195:  (u'GetPCFactionMurder', 2, 0),
    197:  (u'GetPCEnemyofFaction', 2, 0),
    199:  (u'GetPCFactionAttack', 2, 0),
    203:  (u'GetDestroyed', 0, 0),
    214:  (u'HasMagicEffect', 2, 0),
    215:  (u'GetDefaultOpen', 0, 0),
    219:  (u'GetAnimAction', 0, 0),
    223:  (u'IsSpellTarget', 2, 0),
    224:  (u'GetVATSMode', 0, 0),
    225:  (u'GetPersuasionNumber', 0, 0),
    226:  (u'GetVampireFeed', 0, 0),
    227:  (u'GetCannibal', 0, 0),
    228:  (u'GetIsClassDefault', 2, 0),
    229:  (u'GetClassDefaultMatch', 0, 0),
    230:  (u'GetInCellParam', 2, 2),
    235:  (u'GetVatsTargetHeight', 0, 0),
    237:  (u'GetIsGhost', 0, 0),
    242:  (u'GetUnconscious', 0, 0),
    244:  (u'GetRestrained', 0, 0),
    246:  (u'GetIsUsedItem', 2, 0),
    247:  (u'GetIsUsedItemType', 2, 0),
    248:  (u'IsScenePlaying', 2, 0),
    249:  (u'IsInDialogueWithPlayer', 0, 0),
    250:  (u'GetLocationCleared', 2, 0),
    254:  (u'GetIsPlayableRace', 0, 0),
    255:  (u'GetOffersServicesNow', 0, 0),
    258:  (u'HasAssociationType', 2, 2),
    259:  (u'HasFamilyRelationship', 2, 0),
    261:  (u'HasParentRelationship', 2, 0),
    262:  (u'IsWarningAbout', 2, 0),
    263:  (u'IsWeaponOut', 0, 0),
    264:  (u'HasSpell', 2, 0),
    265:  (u'IsTimePassing', 0, 0),
    266:  (u'IsPleasant', 0, 0),
    267:  (u'IsCloudy', 0, 0),
    274:  (u'IsSmallBump', 0, 0),
    277:  (u'GetBaseActorValue', 2, 0),
    278:  (u'IsOwner', 2, 0),
    280:  (u'IsCellOwner', 2, 2),
    282:  (u'IsHorseStolen', 0, 0),
    285:  (u'IsLeftUp', 0, 0),
    286:  (u'IsSneaking', 0, 0),
    287:  (u'IsRunning', 0, 0),
    288:  (u'GetFriendHit', 0, 0),
    289:  (u'IsInCombat', 1, 0),
    300:  (u'IsInInterior', 0, 0),
    304:  (u'IsWaterObject', 0, 0),
    305:  (u'GetPlayerAction', 0, 0),
    306:  (u'IsActorUsingATorch', 0, 0),
    309:  (u'IsXBox', 0, 0),
    310:  (u'GetInWorldspace', 2, 0),
    312:  (u'GetPCMiscStat', 0, 0),
    313:  (u'GetPairedAnimation', 0, 0),
    314:  (u'IsActorAVictim', 0, 0),
    315:  (u'GetTotalPersuasionNumber', 0, 0),
    318:  (u'GetIdleDoneOnce', 0, 0),
    320:  (u'GetNoRumors', 0, 0),
    323:  (u'GetCombatState', 0, 0),
    325:  (u'GetWithinPackageLocation', 0, 0),
    327:  (u'IsRidingMount', 0, 0),
    329:  (u'IsFleeing', 0, 0),
    332:  (u'IsInDangerousWater', 0, 0),
    338:  (u'GetIgnoreFriendlyHits', 0, 0),
    339:  (u'IsPlayersLastRiddenMount', 0, 0),
    353:  (u'IsActor', 0, 0),
    354:  (u'IsEssential', 0, 0),
    358:  (u'IsPlayerMovingIntoNewSpace', 0, 0),
    359:  (u'GetInCurrentLoc', 2, 0),
    360:  (u'GetInCurrentLocAlias', 1, 0),
    361:  (u'GetTimeDead', 0, 0),
    362:  (u'HasLinkedRef', 2, 0),
    365:  (u'IsChild', 0, 0),
    366:  (u'GetStolenItemValueNoCrime', 2, 0),
    367:  (u'GetLastPlayerAction', 0, 0),
    368:  (u'IsPlayerActionActive', 1, 0),
    370:  (u'IsTalkingActivatorActor', 2, 0),
    372:  (u'IsInList', 2, 0),
    373:  (u'GetStolenItemValue', 2, 0),
    375:  (u'GetCrimeGoldViolent', 2, 0),
    376:  (u'GetCrimeGoldNonviolent', 2, 0),
    378:  (u'HasShout', 2, 0),
    381:  (u'GetHasNote', 2, 0),
    390:  (u'GetHitLocation', 0, 0),
    391:  (u'IsPC1stPerson', 0, 0),
    396:  (u'GetCauseofDeath', 0, 0),
    397:  (u'IsLimbGone', 1, 0),
    398:  (u'IsWeaponInList', 2, 0),
    402:  (u'IsBribedbyPlayer', 0, 0),
    403:  (u'GetRelationshipRank', 2, 0),
    # We set the second to 'unused' here to receive it as 4 bytes, which we
    # then handle inside MelCtdaFo3.
    407:  (u'GetVATSValue', 1, 0),
    408:  (u'IsKiller', 2, 0),
    409:  (u'IsKillerObject', 2, 0),
    410:  (u'GetFactionCombatReaction', 2, 2),
    414:  (u'Exists', 2, 0),
    415:  (u'GetGroupMemberCount', 0, 0),
    416:  (u'GetGroupTargetCount', 0, 0),
    426:  (u'GetIsVoiceType', 2, 0),
    427:  (u'GetPlantedExplosive', 0, 0),
    429:  (u'IsScenePackageRunning', 0, 0),
    430:  (u'GetHealthPercentage', 0, 0),
    432:  (u'GetIsObjectType', 2, 0),
    434:  (u'GetDialogueEmotion', 0, 0),
    435:  (u'GetDialogueEmotionValue', 0, 0),
    437:  (u'GetIsCreatureType', 1, 0),
    444:  (u'GetInCurrentLocFormList', 2, 0),
    445:  (u'GetInZone', 2, 0),
    446:  (u'GetVelocity', 0, 0),
    447:  (u'GetGraphVariableFloat', 0, 0),
    448:  (u'HasPerk', 2, 0),
    449:  (u'GetFactionRelation', 2, 0),
    450:  (u'IsLastIdlePlayed', 2, 0),
    453:  (u'GetPlayerTeammate', 0, 0),
    454:  (u'GetPlayerTeammateCount', 0, 0),
    458:  (u'GetActorCrimePlayerEnemy', 0, 0),
    459:  (u'GetCrimeGold', 2, 0),
    463:  (u'IsPlayerGrabbedRef', 2, 0),
    465:  (u'GetKeywordItemCount', 2, 0),
    470:  (u'GetDestructionStage', 0, 0),
    473:  (u'GetIsAlignment', 2, 0),
    476:  (u'IsProtected', 0, 0),
    477:  (u'GetThreatRatio', 2, 0),
    479:  (u'GetIsUsedItemEquipType', 2, 0),
    487:  (u'IsCarryable', 0, 0),
    488:  (u'GetConcussed', 0, 0),
    491:  (u'GetMapMarkerVisible', 0, 0),
    493:  (u'PlayerKnows', 0, 0),
    494:  (u'GetPermanentActorValue', 2, 0),
    495:  (u'GetKillingBlowLimb', 0, 0),
    497:  (u'CanPayCrimeGold', 2, 0),
    499:  (u'GetDaysInJail', 0, 0),
    500:  (u'EPAlchemyGetMakingPoison', 0, 0),
    501:  (u'EPAlchemyEffectHasKeyword', 2, 0),
    503:  (u'GetAllowWorldInteractions', 0, 0),
    508:  (u'GetLastHitCritical', 0, 0),
    513:  (u'IsCombatTarget', 2, 0),
    515:  (u'GetVATSRightAreaFree', 2, 0),
    516:  (u'GetVATSLeftAreaFree', 2, 0),
    517:  (u'GetVATSBackAreaFree', 2, 0),
    518:  (u'GetVATSFrontAreaFree', 2, 0),
    519:  (u'GetIsLockBroken', 0, 0),
    520:  (u'IsPS3', 0, 0),
    521:  (u'IsWin32', 0, 0),
    522:  (u'GetVATSRightTargetVisible', 2, 0),
    523:  (u'GetVATSLeftTargetVisible', 2, 0),
    524:  (u'GetVATSBackTargetVisible', 2, 0),
    525:  (u'GetVATSFrontTargetVisible', 2, 0),
    528:  (u'IsInCriticalStage', 2, 0),
    530:  (u'GetXPForNextLevel', 0, 0),
    533:  (u'GetInfamy', 2, 0),
    534:  (u'GetInfamyViolent', 2, 0),
    535:  (u'GetInfamyNonViolent', 2, 0),
    543:  (u'GetQuestCompleted', 2, 0),
    547:  (u'IsGoreDisabled', 0, 0),
    550:  (u'IsSceneActionComplete', 2, 1),
    552:  (u'GetSpellUsageNum', 2, 0),
    554:  (u'GetActorsInHigh', 0, 0),
    555:  (u'HasLoaded3D', 0, 0),
    560:  (u'HasKeyword', 2, 0),
    561:  (u'HasRefType', 2, 0),
    562:  (u'LocationHasKeyword', 2, 0),
    563:  (u'LocationHasRefType', 2, 0),
    565:  (u'GetIsEditorLocation', 2, 0),
    566:  (u'GetIsAliasRef', 1, 0),
    567:  (u'GetIsEditorLocAlias', 1, 0),
    568:  (u'IsSprinting', 0, 0),
    569:  (u'IsBlocking', 0, 0),
    570:  (u'HasEquippedSpell', 2, 0),
    571:  (u'GetCurrentCastingType', 2, 0),
    572:  (u'GetCurrentDeliveryType', 2, 0),
    574:  (u'GetAttackState', 0, 0),
    576:  (u'GetEventData', 0, 2),
    577:  (u'IsCloserToAThanB', 2, 2),
    579:  (u'GetEquippedShout', 2, 0),
    580:  (u'IsBleedingOut', 0, 0),
    584:  (u'GetRelativeAngle', 2, 0),
    589:  (u'GetMovementDirection', 0, 0),
    590:  (u'IsInScene', 0, 0),
    591:  (u'GetRefTypeDeadCount', 2, 2),
    592:  (u'GetRefTypeAliveCount', 2, 2),
    594:  (u'GetIsFlying', 0, 0),
    595:  (u'IsCurrentSpell', 2, 2),
    596:  (u'SpellHasKeyword', 2, 2),
    597:  (u'GetEquippedItemType', 2, 0),
    598:  (u'GetLocationAliasCleared', 1, 0),
    600:  (u'GetLocAliasRefTypeDeadCount', 1, 2),
    601:  (u'GetLocAliasRefTypeAliveCount', 1, 2),
    602:  (u'IsWardState', 0, 0),
    603:  (u'IsInSameCurrentLocAsRef', 2, 2),
    604:  (u'IsInSameCurrentLocAsRefAlias', 1, 2),
    605:  (u'LocAliasIsLocation', 1, 2),
    606:  (u'GetKeywordDataForLocation', 2, 2),
    608:  (u'GetKeywordDataForAlias', 1, 2),
    610:  (u'LocAliasHasKeyword', 1, 2),
    611:  (u'IsNullPackageData', 0, 0),
    612:  (u'GetNumericPackageData', 0, 0),
    613:  (u'IsFurnitureAnimType', 0, 0),
    614:  (u'IsFurnitureEntryType', 0, 0),
    615:  (u'GetHighestRelationshipRank', 0, 0),
    616:  (u'GetLowestRelationshipRank', 0, 0),
    617:  (u'HasAssociationTypeAny', 2, 0),
    618:  (u'HasFamilyRelationshipAny', 0, 0),
    619:  (u'GetPathingTargetOffset', 0, 0),
    620:  (u'GetPathingTargetAngleOffset', 0, 0),
    621:  (u'GetPathingTargetSpeed', 0, 0),
    622:  (u'GetPathingTargetSpeedAngle', 0, 0),
    623:  (u'GetMovementSpeed', 0, 0),
    624:  (u'GetInContainer', 2, 0),
    625:  (u'IsLocationLoaded', 2, 0),
    626:  (u'IsLocAliasLoaded', 1, 0),
    627:  (u'IsDualCasting', 0, 0),
    629:  (u'GetVMQuestVariable', 2, 0),
    630:  (u'GetVMScriptVariable', 2, 0),
    631:  (u'IsEnteringInteractionQuick', 0, 0),
    632:  (u'IsCasting', 0, 0),
    633:  (u'GetFlyingState', 0, 0),
    635:  (u'IsInFavorState', 0, 0),
    636:  (u'HasTwoHandedWeaponEquipped', 0, 0),
    637:  (u'IsExitingInstant', 0, 0),
    638:  (u'IsInFriendStatewithPlayer', 0, 0),
    639:  (u'GetWithinDistance', 2, 3),
    640:  (u'GetActorValuePercent', 2, 0),
    641:  (u'IsUnique', 0, 0),
    642:  (u'GetLastBumpDirection', 0, 0),
    644:  (u'IsInFurnitureState', 0, 0),
    645:  (u'GetIsInjured', 0, 0),
    646:  (u'GetIsCrashLandRequest', 0, 0),
    647:  (u'GetIsHastyLandRequest', 0, 0),
    650:  (u'IsLinkedTo', 2, 2),
    651:  (u'GetKeywordDataForCurrentLocation', 2, 0),
    652:  (u'GetInSharedCrimeFaction', 2, 0),
    654:  (u'GetBribeSuccess', 0, 0),
    655:  (u'GetIntimidateSuccess', 0, 0),
    656:  (u'GetArrestedState', 0, 0),
    657:  (u'GetArrestingActor', 0, 0),
    659:  (u'EPTemperingItemIsEnchanted', 0, 0),
    660:  (u'EPTemperingItemHasKeyword', 2, 0),
    664:  (u'GetReplacedItemType', 2, 0),
    672:  (u'IsAttacking', 0, 0),
    673:  (u'IsPowerAttacking', 0, 0),
    674:  (u'IsLastHostileActor', 0, 0),
    675:  (u'GetGraphVariableInt', 0, 0),
    676:  (u'GetCurrentShoutVariation', 0, 0),
    678:  (u'ShouldAttackKill', 2, 0),
    680:  (u'GetActivationHeight', 0, 0),
    681:  (u'EPModSkillUsage_IsAdvanceSkill', 2, 0),
    682:  (u'WornHasKeyword', 2, 0),
    683:  (u'GetPathingCurrentSpeed', 0, 0),
    684:  (u'GetPathingCurrentSpeedAngle', 0, 0),
    691:  (u'EPModSkillUsage_AdvanceObjectHasKeyword', 2, 0),
    692:  (u'EPModSkillUsage_IsAdvanceAction', 0, 0),
    693:  (u'EPMagic_SpellHasKeyword', 2, 0),
    694:  (u'GetNoBleedoutRecovery', 0, 0),
    696:  (u'EPMagic_SpellHasSkill', 2, 0),
    697:  (u'IsAttackType', 2, 0),
    698:  (u'IsAllowedToFly', 0, 0),
    699:  (u'HasMagicEffectKeyword', 2, 0),
    700:  (u'IsCommandedActor', 0, 0),
    701:  (u'IsStaggered', 0, 0),
    702:  (u'IsRecoiling', 0, 0),
    703:  (u'IsExitingInteractionQuick', 0, 0),
    704:  (u'IsPathing', 0, 0),
    705:  (u'GetShouldHelp', 2, 0),
    706:  (u'HasBoundWeaponEquipped', 2, 0),
    707:  (u'GetCombatTargetHasKeyword', 2, 0),
    709:  (u'GetCombatGroupMemberCount', 0, 0),
    710:  (u'IsIgnoringCombat', 0, 0),
    711:  (u'GetLightLevel', 0, 0),
    713:  (u'SpellHasCastingPerk', 2, 0),
    714:  (u'IsBeingRidden', 0, 0),
    715:  (u'IsUndead', 0, 0),
    716:  (u'GetRealHoursPassed', 0, 0),
    718:  (u'IsUnlockedDoor', 0, 0),
    719:  (u'IsHostileToActor', 2, 0),
    720:  (u'GetTargetHeight', 2, 0),
    721:  (u'IsPoison', 0, 0),
    722:  (u'WornApparelHasKeywordCount', 2, 0),
    723:  (u'GetItemHealthPercent', 0, 0),
    724:  (u'EffectWasDualCast', 0, 0),
    725:  (u'GetKnockStateEnum', 0, 0),
    726:  (u'DoesNotExist', 0, 0),
    730:  (u'IsOnFlyingMount', 0, 0),
    731:  (u'CanFlyHere', 0, 0),
    732:  (u'IsFlyingMountPatrolQueued', 0, 0),
    733:  (u'IsFlyingMountFastTravelling', 0, 0),
    734:  (u'IsOverEncumbered', 0, 0),
    735:  (u'GetActorWarmth', 0, 0),

    # extended by SKSE
    1024: (u'GetSKSEVersion', 0, 0),
    1025: (u'GetSKSEVersionMinor', 0, 0),
    1026: (u'GetSKSEVersionBeta', 0, 0),
    1027: (u'GetSKSERelease', 0, 0),
    1028: (u'ClearInvalidRegistrations', 0, 0),
}
getvatsvalue_index = 407

#------------------------------------------------------------------------------
# Leveled Lists
#------------------------------------------------------------------------------
listTypes = (b'LVLI',b'LVLN',b'LVSP',)

#------------------------------------------------------------------------------
# Import Names
#------------------------------------------------------------------------------
namesTypes = {b'ACTI', b'ALCH', b'AMMO', b'APPA', b'ARMO', b'AVIF', b'BOOK',
              b'CLAS', b'CLFM', b'CONT', b'DOOR', b'ENCH', b'EXPL', b'EYES',
              b'FACT', b'FLOR', b'FURN', b'HAZD', b'HDPT', b'INGR', b'KEYM',
              b'LCTN', b'LIGH', b'MESG', b'MGEF', b'MISC', b'MSTT', b'NPC_',
              b'PERK', b'PROJ', b'RACE', b'SCRL', b'SHOU', b'SLGM', b'SNCT',
              b'SPEL', b'TACT', b'TREE', b'WATR', b'WEAP', b'WOOP'}

#------------------------------------------------------------------------------
# Import Prices
#------------------------------------------------------------------------------
pricesTypes = {b'ALCH', b'AMMO', b'APPA', b'ARMO', b'BOOK', b'INGR', b'KEYM',
               b'LIGH', b'MISC', b'SLGM', b'WEAP'}

#------------------------------------------------------------------------------
# Import Stats
#------------------------------------------------------------------------------
statsTypes = {
        b'ALCH':(u'eid', u'weight', u'value'),
        b'AMMO':(u'eid', u'value', u'damage'),
        b'APPA':(u'eid', u'weight', u'value'),
        b'ARMO':(u'eid', u'weight', u'value', u'armorRating'),
        b'BOOK':(u'eid', u'weight', u'value'),
        b'INGR':(u'eid', u'weight', u'value'),
        b'KEYM':(u'eid', u'weight', u'value'),
        b'LIGH':(u'eid', u'weight', u'value', u'duration'),
        b'MISC':(u'eid', u'weight', u'value'),
        b'SLGM':(u'eid', u'weight', u'value'),
        b'WEAP':(u'eid', u'weight', u'value', u'damage', u'speed', u'reach',
                 u'enchantPoints', u'stagger', u'critDamage',
                 u'criticalMultiplier', u'criticalEffect',),
    }

#------------------------------------------------------------------------------
# Import Sounds
#------------------------------------------------------------------------------
soundsTypes = {
    b'ACTI': (u'soundLooping', u'soundActivation'),
    b'ADDN': (u'ambientSound',),
    b'ALCH': (u'dropSound', u'pickupSound', u'soundConsume'),
    b'AMMO': (u'pickupSound', u'dropSound'),
    b'APPA': (u'pickupSound', u'dropSound'),
    b'ARMA': (u'footstepSound',),
    b'ARMO': (u'pickupSound', u'dropSound'),
    b'ASPC': (u'ambientSound', u'regionData', u'reverb'),
    b'BOOK': (u'pickupSound', u'dropSound'),
    b'CONT': (u'soundOpen', u'soundClose'),
    b'DOOR': (u'soundOpen', u'soundClose', u'soundLoop'),
    b'EFSH': (u'ambientSound',),
    b'EXPL': (u'sound1', u'sound2'),
    b'FLOR': (u'harvestSound',),
    b'HAZD': (u'sound',),
    b'INGR': (u'pickupSound', u'dropSound'),
    b'IPCT': (u'sound1', u'sound2'),
    b'KEYM': (u'pickupSound', u'dropSound'),
    b'LIGH': (u'sound',),
    #Needs to loop over all the sounds
    b'MGEF': (u'sounds', u'casting_sound_level'),
    # b'REGN': (u'entries',),
    b'MISC': (u'pickupSound', u'dropSound'),
    b'MSTT': (u'sound',),
    b'SCRL': (u'pickupSound', u'dropSound'),
    b'SLGM': (u'pickupSound', u'dropSound'),
    b'SNCT': (u'parent', u'staticVolumeMultiplier'),
    # Sounds does not need to loop here
    b'SNDR': (u'category', u'outputModel', u'sounds', u'looping',
              u'rumbleSendValue', u'pctFrequencyShift',
              u'pctFrequencyVariance', u'priority', u'dbVariance',
              u'staticAtten'),
    b'SOPM': (u'reverbSendpct', u'outputType', u'ch0_l', u'ch0_r', u'ch0_c',
              u'ch0_lFE', u'ch0_rL', u'ch0_rR', u'ch0_bL', u'ch0_bR', u'ch1_l',
              u'ch1_r', u'ch1_c', u'ch1_lFE', u'ch1_rL', u'ch1_rR', u'ch1_bL',
              u'ch1_bR', u'ch2_l', u'ch2_r', u'ch2_c', u'ch2_lFE', u'ch2_rL',
              u'ch2_rR', u'ch2_bL', u'ch2_bR', u'minDistance', u'maxDistance',
              u'curve1', u'curve2', u'curve3', u'curve4', u'curve5'),
    b'SOUN': (u'soundDescriptor',),
    b'TACT': (u'soundLoop',),
    b'TREE': (u'harvestSound',),
    b'WATR': (u'openSound',),
    b'WEAP': (u'pickupSound', u'dropSound', u'attackSound', u'attackSound2D',
              u'attackLoopSound', u'attackFailSound', u'idleSound',
              u'equipSound', u'unequipSound', u'detectionSoundLevel'),
    #Needs to loop over all the sounds
    b'WTHR': (u'sounds',),
}

#------------------------------------------------------------------------------
# Import Cells
#------------------------------------------------------------------------------
cellRecAttrs = {
    u'C.Acoustic': (u'acousticSpace',),
    u'C.Climate': (u'climate', u'flags.showSky'),
    u'C.Encounter': (u'encounterZone',),
    u'C.ForceHideLand': (u'land_flags',),
    u'C.ImageSpace': (u'imageSpace',),
    ##: Patches unused?
    u'C.Light': (u'ambientRed', u'ambientGreen', u'ambientBlue', u'unused1',
                 u'directionalRed', u'directionalGreen', u'directionalBlue',
                 u'unused2', u'fogRed', u'fogGreen', u'fogBlue', u'unused3',
                 u'fogNear', u'fogFar', u'directionalXY', u'directionalZ',
                 u'directionalFade', u'fogClip', u'fogPower', u'redXplus',
                 u'greenXplus', u'blueXplus', u'unknownXplus', u'redXminus',
                 u'greenXminus', u'blueXminus', u'unknownXminus', u'redYplus',
                 u'greenYplus', u'blueYplus', u'unknownYplus', u'redYminus',
                 u'greenYminus', u'blueYminus', u'unknownYminus', u'redZplus',
                 u'greenZplus', u'blueZplus', u'unknownZplus', u'redZminus',
                 u'greenZminus', u'blueZminus', u'unknownZminus', u'redSpec',
                 u'greenSpec', u'blueSpec', u'unknownSpec', u'fresnelPower',
                 u'fogColorFarRed', u'fogColorFarGreen', u'fogColorFarBlue',
                 u'unused4', u'fogMax', u'lightFadeBegin', u'lightFadeEnd',
                 u'inherits', u'lightTemplate',),
    u'C.Location': (u'location',),
    u'C.LockList': (u'lockList',),
    u'C.MiscFlags': (u'flags.isInterior', u'flags.cantFastTravel',
                     u'flags.noLODWater', u'flags.handChanged'),
    u'C.Music': (u'music',),
    u'C.Name': (u'full',),
    u'C.Owner': (u'ownership', u'flags.publicPlace'),
    u'C.RecordFlags': (u'flags1',), # Yes seems funky but thats the way it is
    u'C.Regions': (u'regions',),
    u'C.SkyLighting': (u'skyFlags.useSkyLighting',),
    u'C.Water': (u'water', u'waterHeight', u'waterNoiseTexture',
                 u'waterEnvironmentMap', u'flags.hasWater'),
}
cell_skip_interior_attrs = {u'waterHeight'}

#------------------------------------------------------------------------------
# Import Graphics
#------------------------------------------------------------------------------
graphicsTypes = {
    b'ACTI': (u'model',),
    b'ALCH': (u'iconPath', u'model'),
    b'AMMO': (u'iconPath', u'model'),
    b'APPA': (u'iconPath', u'model'),
    b'ARMA': (u'male_model', u'female_model', u'male_model_1st',
              u'female_model_1st', u'biped_flags'),
    b'ARMO': (u'model2', u'maleIconPath', u'model4', u'femaleIconPath',
              u'addons', u'biped_flags'),
    b'BOOK': (u'iconPath', u'model'),
    b'CLAS': (u'iconPath',),
    b'CONT': (u'model',),
    b'DOOR': (u'model',),
    b'EFSH': (u'unused1', u'memSBlend', u'memBlendOp', u'memZFunc', u'fillRed',
              u'fillGreen', u'fillBlue', u'unused2', u'fillAlphaIn',
              u'fillFullAlpha', u'fillAlphaOut', u'fillAlphaRatio',
              u'fillAlphaAmp', u'fillAlphaPulse', u'fillAnimSpeedU',
              u'fillAnimSpeedV', u'edgeEffectOff', u'edgeRed', u'edgeGreen',
              u'edgeBlue', u'unused3', u'edgeAlphaIn', u'edgeFullAlpha',
              u'edgeAlphaOut', u'edgeAlphaRatio', u'edgeAlphaAmp',
              u'edgeAlphaPulse', u'fillFullAlphaRatio', u'edgeFullAlphaRatio',
              u'memDestBlend', u'partSourceBlend', u'partBlendOp',
              u'partZTestFunc', u'partDestBlend', u'partBSRampUp',
              u'partBSFull', u'partBSRampDown', u'partBSRatio',
              u'partBSPartCount', u'partBSLifetime', u'partBSLifetimeDelta',
              u'partSSpeedNorm', u'partSAccNorm', u'partSVel1', u'partSVel2',
              u'partSVel3', u'partSAccel1', u'partSAccel2', u'partSAccel3',
              u'partSKey1', u'partSKey2', u'partSKey1Time', u'partSKey2Time',
              u'key1Red', u'key1Green', u'key1Blue', u'unused4', u'key2Red',
              u'key2Green', u'key2Blue', u'unused5', u'key3Red', u'key3Green',
              u'key3Blue', u'unused6', u'colorKey1Alpha', u'colorKey2Alpha',
              u'colorKey3Alpha', u'colorKey1KeyTime', u'colorKey2KeyTime',
              u'colorKey3KeyTime', u'partSSpeedNormDelta', u'partSSpeedRotDeg',
              u'partSSpeedRotDegDelta', u'partSRotDeg', u'partSRotDegDelta',
              u'holesStart', u'holesEnd', u'holesStartVal', u'holesEndVal',
              u'edgeWidthAlphaUnit', u'edgeAlphRed', u'edgeAlphGreen',
              u'edgeAlphBlue', u'unused7', u'expWindSpeed', u'textCountU',
              u'textCountV', u'addonModelIn', u'addonModelOut',
              u'addonScaleStart', u'addonScaleEnd', u'addonScaleIn',
              u'addonScaleOut', u'ambientSound', u'key2FillRed',
              u'key2FillGreen', u'key2FillBlue', u'unused8', u'key3FillRed',
              u'key3FillGreen', u'key3FillBlue', u'unused9', u'key1ScaleFill',
              u'key2ScaleFill', u'key3ScaleFill', u'key1FillTime',
              u'key2FillTime', u'key3FillTime', u'colorScale',
              u'birthPosOffset', u'birthPosOffsetRange', u'startFrame',
              u'startFrameVariation', u'endFrame', u'loopStartFrame',
              u'loopStartVariation', u'frameCount', u'frameCountVariation',
              u'flags', u'fillTextScaleU', u'fillTextScaleV',
              u'sceneGraphDepthLimit', u'fillTexture', u'particleTexture',
              u'holesTexture', u'membranePaletteTexture',
              u'particlePaletteTexture'),
    b'FLOR': (u'model',),
    b'FURN': (u'model',),
    b'GRAS': (u'model',),
    b'INGR': (u'iconPath', u'model'),
    b'KEYM': (u'iconPath', u'model'),
    b'LIGH': (u'iconPath', u'model'),
    b'LSCR': (u'iconPath',),
    b'MGEF': (u'dual_casting_scale',),
    b'MISC': (u'iconPath', u'model'),
    b'PERK': (u'iconPath',),
    b'SLGM': (u'iconPath', u'model'),
    b'STAT': (u'model',),
    b'TREE': (u'model',),
    b'WEAP': (u'model1', u'model2', u'iconPath'),
    b'WTHR': (u'wthrAmbientColors',),
}
graphicsFidTypes = {
    b'BOOK': (u'inventoryArt',),
    b'EFSH': (u'addonModels',),
    b'MGEF': (u'menu_display_object', u'light', u'hit_shader',
              u'enchant_shader', u'projectile', u'explosion', u'casting_art',
              u'hit_effect_art', u'effect_impact_data', u'dual_casting_art',
              u'enchant_art', u'hit_visuals', u'enchant_visuals',
              u'effect_imad'),
    b'SCRL': (u'menu_display_object',),
    b'SPEL': (u'menu_display_object',),
    b'WEAP': (u'firstPersonModelObject',),
}
graphicsModelAttrs = (u'model', u'model1', u'model2', u'model4', u'male_model',
                      u'female_model', u'male_model_1st', u'female_model_1st')

#------------------------------------------------------------------------------
# Import Inventory
#------------------------------------------------------------------------------
inventoryTypes = (b'NPC_',b'CONT',)

#------------------------------------------------------------------------------
# Import Keywords
#------------------------------------------------------------------------------
keywords_types = (b'ACTI', b'ALCH', b'AMMO', b'ARMO', b'BOOK', b'FLOR',
                  b'FURN', b'INGR', b'KEYM', b'LCTN', b'MGEF', b'MISC',
                  b'NPC_', b'RACE', b'SCRL', b'SLGM', b'SPEL', b'TACT',
                  b'WEAP',)

#------------------------------------------------------------------------------
# Import Text
#------------------------------------------------------------------------------
text_types = {
    b'ACTI': (u'activate_text_override',),
    b'ALCH': (u'description',),
    b'AMMO': (u'description',),
    b'APPA': (u'description',),
    b'ARMO': (u'description',),
    b'AVIF': (u'description',),
    b'BOOK': (u'description', u'book_text'),
    b'CLAS': (u'description',),
    #b'COLL': (u'description',), # seems fairly useless to patch this
    b'LSCR': (u'description',),
    b'MESG': (u'description',),
    b'MGEF': (u'magic_item_description',),
    b'PERK': (u'description',),
    #b'QUST': (u'description',), # no other patchers and seems unused
    # omit RACE - covered by R.Description
    b'SCRL': (u'description',),
    b'SHOU': (u'description',),
    b'SPEL': (u'description',),
    b'WEAP': (u'description',),
}

#------------------------------------------------------------------------------
# Import Object Bounds
#------------------------------------------------------------------------------
object_bounds_types = {b'ACTI', b'ADDN', b'ALCH', b'AMMO', b'APPA', b'ARMO',
                       b'ARTO', b'ASPC', b'BOOK', b'CONT', b'DOOR', b'DUAL',
                       b'ENCH', b'EXPL', b'FLOR', b'FURN', b'GRAS', b'HAZD',
                       b'IDLM', b'INGR', b'KEYM', b'LIGH', b'LVLI', b'LVLN',
                       b'LVSP', b'MISC', b'MSTT', b'NPC_', b'PROJ', b'SCRL',
                       b'SLGM', b'SOUN', b'SPEL', b'STAT', b'TACT', b'TREE',
                       b'TXST', b'WEAP'}

#------------------------------------------------------------------------------
# Contents Checker
#------------------------------------------------------------------------------
# Entry types used for COBJ, CONT, LVLI and NPC_
_common_entry_types = {b'ALCH', b'AMMO', b'APPA', b'ARMO', b'BOOK', b'INGR',
                       b'KEYM', b'LIGH', b'LVLI', b'MISC', b'SLGM', b'SCRL',
                       b'WEAP'}
cc_valid_types = {
    b'COBJ': _common_entry_types,
    b'CONT': _common_entry_types,
    b'LVLN': {b'LVLN', b'NPC_'},
    b'LVLI': _common_entry_types,
    b'LVSP': {b'LVSP', b'SPEL'},
    b'NPC_': _common_entry_types,
    b'OTFT': {b'ARMO', b'LVLI'},
}
cc_passes = (
    ((b'LVLN', b'LVLI', b'LVSP'), 'entries', 'listId'),
    ((b'COBJ', b'CONT', b'NPC_'), 'items', 'item'),
    ((b'OTFT',), 'items'),
)

#------------------------------------------------------------------------------
# Import Destructible
#------------------------------------------------------------------------------
destructible_types = {b'ACTI', b'ALCH', b'AMMO', b'APPA', b'ARMO', b'BOOK',
                      b'CONT', b'DOOR', b'FLOR', b'FURN', b'KEYM', b'LIGH',
                      b'MISC', b'MSTT', b'NPC_', b'PROJ', b'SCRL', b'SLGM',
                      b'TACT', b'WEAP'}

#------------------------------------------------------------------------------
# Import Actors
#------------------------------------------------------------------------------
actor_importer_attrs = {
    b'NPC_': {
        u'Actors.ACBS': (u'bleedoutOverride', u'calcMax', u'calcMin',
                         u'dispositionBase', u'flags.autoCalc',
                         u'flags.bleedoutOverride',
                         u'flags.doesNotAffectStealth', u'flags.doesNotBleed',
                         u'flags.essential', u'flags.female',
                         u'flags.invulnerable', u'flags.isCharGenFacePreset',
                         u'flags.isGhost', u'flags.loopedAudio',
                         u'flags.loopedScript', u'flags.oppositeGenderAnims',
                         u'flags.pcLevelMult', u'flags.protected',
                         u'flags.respawn', u'flags.simpleActor',
                         u'flags.summonable', u'flags.unique', u'healthOffset',
                         u'level_offset', u'magickaOffset', u'speedMultiplier',
                         u'staminaOffset'),
        u'Actors.AIData': (u'aggression', u'aggroRadiusBehavior',
                           u'assistance', u'attack', u'confidence',
                           u'energyLevel', u'mood', u'responsibility', u'warn',
                           u'warnAttack'),
        u'Actors.CombatStyle': (u'combatStyle',),
        u'Actors.RecordFlags': (u'flags1',),
        u'Actors.Stats': (u'alchemySO', u'alchemySV', u'alterationSO',
                          u'alterationSV', u'blockSO', u'blockSV',
                          u'conjurationSO', u'conjurationSV', u'destructionSO',
                          u'destructionSV', u'enchantingSO', u'enchantingSV',
                          u'health', u'heavyArmorSO', u'heavyArmorSV',
                          u'illusionSO', u'illusionSV', u'lightArmorSO',
                          u'lightArmorSV', u'lockpickingSO', u'lockpickingSV',
                          u'magicka', u'marksmanSO', u'marksmanSV',
                          u'oneHandedSO', u'oneHandedSV', u'pickpocketSO',
                          u'pickpocketSV', u'restorationSO', u'restorationSV',
                          u'smithingSO', u'smithingSV', u'sneakSO', u'sneakSV',
                          u'speechcraftSO', u'speechcraftSV', u'stamina',
                          u'twoHandedSO', u'twoHandedSV'),
        u'Actors.Voice': (u'voice',),
        u'NPC.AIPackageOverrides': (u'spectator', u'observe', u'guardWarn',
                                    u'combat'),
        u'NPC.AttackRace': (u'attackRace',),
        u'NPC.Class': (u'iclass',),
        u'NPC.CrimeFaction': (u'crime_faction',),
        u'NPC.DefaultOutfit': (u'default_outfit',),
        u'NPC.Race': (u'race',),
    },
}
actor_types = (b'NPC_',)

#------------------------------------------------------------------------------
# Import Spell Stats
#------------------------------------------------------------------------------
spell_stats_attrs = (u'eid', u'cost', u'spellType', u'chargeTime', u'castType',
                     u'targetType', u'castDuration', u'range', u'halfCostPerk',
                     u'dataFlags')
spell_stats_types = {b'SCRL', b'SPEL'}

#------------------------------------------------------------------------------
# Tweak Actors
#------------------------------------------------------------------------------
actor_tweaks = {
    u'OppositeGenderAnimsPatcher_Female',
    u'OppositeGenderAnimsPatcher_Male',
}

#------------------------------------------------------------------------------
# Tweak Assorted
#------------------------------------------------------------------------------
assorted_tweaks = {
    u'AssortedTweak_ArmorPlayable',
    u'AssortedTweak_NoLightFlicker',
    u'AssortedTweak_PotionWeight',
    u'AssortedTweak_IngredientWeight',
    u'AssortedTweak_PotionWeightMinimum',
    u'AssortedTweak_StaffWeight',
    u'AssortedTweak_HarvestChance',
    u'AssortedTweak_WindSpeed',
    u'AssortedTweak_UniformGroundcover',
    u'AssortedTweak_SetSoundAttenuationLevels',
    u'AssortedTweak_SetSoundAttenuationLevels_NirnrootOnly',
    u'AssortedTweak_LightFadeValueFix',
    u'AssortedTweak_TextlessLSCRs',
    u'AssortedTweak_AllWaterDamages',
    u'AssortedTweak_AbsorbSummonFix',
    u'AssortedTweak_BookWeight',
}
staff_condition = (u'animationType', 8)

#------------------------------------------------------------------------------
# Tweak Settings
#------------------------------------------------------------------------------
settings_tweaks = {
    u'GlobalsTweak_Timescale_Tes5',
    u'GmstTweak_Msg_SoulCaptured',
    u'GmstTweak_Actor_StrengthEncumbranceMultiplier',
    u'GmstTweak_AI_MaxActiveActors_Tes5',
    u'GmstTweak_Arrow_RecoveryFromActor_Tes5',
    u'GmstTweak_Arrow_Speed',
    u'GmstTweak_World_CellRespawnTime_Tes5',
    u'GmstTweak_World_CellRespawnTime_Cleared',
    u'GmstTweak_Combat_Alchemy',
    u'GmstTweak_Combat_MaxActors_Tes5',
    u'GmstTweak_Combat_RechargeWeapons',
    u'GmstTweak_Actor_MaxCompanions',
    u'GmstTweak_Crime_AlarmDistance',
    u'GmstTweak_Bounty_Assault_Tes5',
    u'GmstTweak_Crime_PrisonDurationModifier',
    u'GmstTweak_Bounty_Jailbreak_Tes5',
    u'GmstTweak_Bounty_Murder',
    u'GmstTweak_Bounty_Pickpocketing',
    u'GmstTweak_Bounty_Trespassing_Tes5',
    u'GmstTweak_Magic_MaxResistance',
    u'GmstTweak_Magic_MaxSummons',
    u'GmstTweak_Actor_VerticalObjectDetection',
    u'GmstTweak_Actor_MaxJumpHeight',
    u'GmstTweak_Player_FastTravelTimeMultiplier',
    u'GmstTweak_Combat_CriticalHitChance',
    u'GmstTweak_Actor_UnconsciousnessDuration',
    u'GmstTweak_Compass_RecognitionDistance',
    u'GmstTweak_Player_HorseTurningSpeed',
    u'GmstTweak_Camera_PCDeathTime',
    u'GmstTweak_Actor_GreetingDistance',
    u'GmstTweak_Bounty_HorseTheft_Tes5',
    u'GmstTweak_Player_InventoryQuantityPrompt',
    u'GmstTweak_Player_MaxDraggableWeight_Tes5',
    u'GmstTweak_Warning_InteriorDistanceToHostiles',
    u'GmstTweak_Warning_ExteriorDistanceToHostiles',
    u'GmstTweak_Combat_MaximumArmorRating_Tes5',
    u'GmstTweak_Arrow_MaxArrowsAttachedToNPC',
    u'GmstTweak_Combat_DisableProjectileDodging',
    u'GmstTweak_Combat_MaxAllyHitsInCombat',
    u'GmstTweak_Combat_MaxAllyHitsOutOfCombat',
    u'GmstTweak_Actor_MerchantRestockTime',
    u'GmstTweak_Player_FallDamageThreshold',
    u'GmstTweak_Player_SprintingCost',
    u'GmstTweak_Visuals_MasserSize',
    u'GmstTweak_Visuals_MasserSpeed',
    u'GmstTweak_Visuals_SecundaSize',
    u'GmstTweak_Visuals_SecundaSpeed',
    u'GmstTweak_AI_BumpReactionDelay',
    u'GmstTweak_Magic_MaxActiveRunes',
    u'GmstTweak_Crime_PickpocketingChance',
    u'GmstTweak_Actor_FasterShouts',
    u'GmstTweak_Combat_FasterTwo_HandedWeapons',
    u'GmstTweak_Actor_TrainingLimit_Tes5',
    u'GmstTweak_Player_UnderwaterBreathControl',
    u'GmstTweak_Combat_StealthDamageBonus',
    u'GmstTweak_Msg_CannotEquipItemFix',
    u'GmstTweak_Msg_AutoSaving',
    u'GmstTweak_Msg_NoFastTravel',
    u'GmstTweak_Msg_QuickLoad',
    u'GmstTweak_Msg_QuickSave',
    u'GmstTweak_Msg_NotEnoughCharge_Tes5',
    u'GmstTweak_Msg_CarryingTooMuch',
    u'GmstTweak_CostMultiplier_Enchantment',
    u'GmstTweak_Magic_InvisibilityDetectionDifficulty',
    u'GmstTweak_Bounty_Shapeshifting',
    u'GmstTweak_SoulTrap_LesserSoulLevel',
    u'GmstTweak_SoulTrap_CommonSoulLevel',
    u'GmstTweak_SoulTrap_GreaterSoulLevel',
    u'GmstTweak_SoulTrap_GrandSoulLevel',
    u'GmstTweak_AI_ConversationChance_Tes5',
    u'GmstTweak_AI_ConversationChance_Interior',
    u'GmstTweak_AI_MaxDeadActors',
    u'GmstTweak_Bounty_Theft',
    u'GmstTweak_Prompt_Activate',
    u'GmstTweak_Prompt_Open',
    u'GmstTweak_Prompt_Read',
    u'GmstTweak_Prompt_Sit',
    u'GmstTweak_Prompt_Take',
    u'GmstTweak_Prompt_Talk',
    u'GmstTweak_Msg_NoSoulGemLargeEnough',
    u'GmstTweak_Combat_SpeakOnHitChance',
    u'GmstTweak_Combat_SpeakOnHitThreshold',
    u'GmstTweak_Combat_MaxFriendHitsInCombat',
    u'GmstTweak_Combat_MaxFriendHitsOutOfCombat',
}

#------------------------------------------------------------------------------
# Import Relations
#------------------------------------------------------------------------------
relations_attrs = (u'faction', u'mod', u'group_combat_reaction')
relations_csv_header = (
    _(u'Main Eid'), _(u'Main Mod'), _(u'Main Object'), _(u'Other Eid'),
    _(u'Other Mod'), _(u'Other Object'), _(u'Modifier'),
    _(u'Group Combat Reaction'))
relations_csv_row_format = u'"%s","%s","0x%06X","%s","%s","0x%06X","%s","%s"\n'

#------------------------------------------------------------------------------
# Import Enchantment Stats
#------------------------------------------------------------------------------
ench_stats_attrs = (u'enchantmentCost', u'generalFlags', u'castType',
                    u'enchantmentAmount', u'targetType', u'enchantType',
                    u'chargeTime', u'baseEnchantment', u'wornRestrictions')

#------------------------------------------------------------------------------
# Import Effect Stats
#------------------------------------------------------------------------------
mgef_stats_attrs = (u'flags', u'base_cost', u'associated_item', u'magic_skill',
                    u'resist_value', u'taper_weight', u'minimum_skill_level',
                    u'spellmaking_area', u'spellmaking_casting_time',
                    u'taper_curve', u'taper_duration', u'second_av_weight',
                    u'effect_archetype', u'actorValue', u'casting_type',
                    u'delivery', u'second_av', u'skill_usage_multiplier',
                    u'equip_ability', u'perk_to_apply',
                    u'script_effect_ai_score', u'script_effect_ai_delay_time')

#------------------------------------------------------------------------------
# Import Races
#------------------------------------------------------------------------------
import_races_attrs = {
    b'RACE': {
        u'R.Body-Size-F': (u'femaleHeight', u'femaleWeight'),
        u'R.Body-Size-M': (u'maleHeight', u'maleWeight'),
        u'R.Description': (u'description',),
        u'R.Skills': (u'skills',),
        u'R.Stats': (u'starting_health', u'starting_magicka',
                     u'starting_stamina', u'base_carry_weight',
                     u'health_regen', u'magicka_regen', u'stamina_regen',
                     u'unarmed_damage', u'unarmed_reach'),
        u'R.Voice-F': (u'femaleVoice',),
        u'R.Voice-M': (u'maleVoice',),
    },
}

#------------------------------------------------------------------------------
# Import Enchantments
#------------------------------------------------------------------------------
enchantment_types = {b'ARMO', b'EXPL', b'WEAP'}

#------------------------------------------------------------------------------
# Tweak Races
#------------------------------------------------------------------------------
race_tweaks = {
    u'RaceTweak_PlayableHeadParts',
    u'RaceTweak_GenderlessHeadParts',
    u'RaceTweak_ForceBehaviorGraphGender_Female',
    u'RaceTweak_ForceBehaviorGraphGender_Male',
}

#------------------------------------------------------------------------------
# Timescale Checker
#------------------------------------------------------------------------------
# Same story as in Nehrim for Enderal too - devs changed timescale, but forgot
# to adjust wave periods. So keep at 20 for Enderal.
default_wp_timescale = 20
