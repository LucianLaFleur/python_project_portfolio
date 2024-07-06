# CLEARLY MARKED AS HOMEBREW
#  Based on Xanthar's guide to Everything, DnD 5e -- This is for educational purposes only, and I have no affiliations, nor do I profit from this.
# ---
# This assumes you have a battlemap or some other way of tracking who to target and what is on the field.
#       This program is for calculations, and not for mapping out positioning
# ---
#  Difference log : 1) Higher chance for chaos-jumping (12.5% --> 33 %)
#                   12.5% chance on 2d8, which means only once out of every 8 casts of a lvl1 spell... not likely at all.
#  NYI              Exchanged for raw 50% chance of chaining (since separate attack rolls are needed, it's more fair and more engaging; should be easier to chain enemies who you got advantage on, encouraging tactics)
#                   roll 1d6, on 5 or 6 jump (instead of the 2d8 having to align)
#                   2) Chaotic variance: instead of 8 possible outcomes, 15 possiblilities exist for damage types                  
#                   3) jumping energy prioritizes living target > matching (fire burns, electric conducts in water, etc.) > destructable target (rope, wall, door) > doing nothing
#                       This priority must be taken in consideration when looking at the battlemap (positioning cannot be automated via CLI)
#                   4) Can declare intention to cast in damage mode or debuff mode; 12.5% chance (1/8) that the opposite mode will be chosen instead

# homebrew suggestions : A sorcery point can be spent to choose the element for the next 5 minutes of casting Improved Chaos Bolt
#                       Alternatively, a monk with magic initiate can do so for 1 ki point, if they take this spell
# ---
import random

core_stats_list = [
    "Strength",
    "Dexterity",
    "Constitution",
    "Intelligence",
    "Wisdom",
    "Charisma"
]

rand_polymorph_list_CR_1_enemy = [
    "slug 4AC, 1HP, 5climb",
    "housefly 14AC, 1HP, 60fly",
    "wasp 14AC, 1HP, 1d4 (4 atk), 60fly",
    "glowing beetle 10AC, 6HP, 30climb",
    "large dog, 12AC, 11HP, 40ft, +3hit, 1d6+1",
    "wolf, 13AC, 12HP, 40ft, +4 hit, 2d4+2",
    "axe beak, 11AC, 15HP, 50ft, str2, dex1, con1, 1d8+2 (+4hit) slash",
    "poison centipede (5ft long), 12AC, 9HP, 30ft climb, str -2, dex 2, (+4hit) 1d4 pierce + 2d6 poison (DC 11 half)",
    "giant rat, 13 AC, 6HP, -2 str, 2 dex, darkvision 60, +4 hit, 1d4 + 2 DAM",
    "bull, 10AC, 18 HP, 4 str, charge 20ft move for extra 1d6 pierce dc 13 STR or prone, +4 hit, 1d6 + 4",
    "Black bear, 11AC, 22HP, climb30, Multiattack 2 bite, claw (atk+3), 1d6 + 2 dam",
    "ape, 12AC, 21HP, climb 30, 3str, 2 dex, athl. 5, multiattack (atk + 5) 1d6 + 3 blunt (can throw rocks for this dam. too)",
    "giant snake, 13AC, 36HP, Multiattack2, 1d8+3 (+4hit) blunt (DC 12 grapple), 40swim",
    "giant spider, 14AC, 24HP, web (60ft, 25ft cube), (+4hit) 1d6 pierce + 2d6 poison (dc12 half), 40ft climb",
    "clone stats of random player; becomes a copy of them"
]

# subject to change/expand, so left as a list
chaos_debuff_list = [
    # !! Keyword "damage" is used to roll for element and damage if a debuff type is chosen
    # When adding descriptions, avoid using the word "damage" or else current logic will trigger a damage rolll
    "[Make Vuln.] damage, but next damage taken is doubled",
    "[Give Adv.] damage, next attack made on target is with advantage",
    "[Restrain] damage, target is restrained for 1 turn",
    "[slow] damage, movement reduced by half",
    "[Pain resonance] damage inflicted against target and the same on another enemy\n or closest ally if no other enemies are present",
    "[Demolition] damage target to nearest destructable object/\n or enemy shield/armor -2 AC \n or ally armor/direct DMG if no armor",
    "[Disarm] damage, then disable/drop weapon if they have one \n if no weapon, disable a multiattack, else no effect.",
    "[Blinding strike] damage, target blinded 1 turn", 
    "[Deaf-mute] damage, target deafened and silenced for 1 turn",
# ========================================      ========================================        ========================================
# ========== No "damage" keywords below, heavier effects below are balanced for not taking direct damage from the spell ================
# ========================================      ========================================        ========================================
    "[Flat-prone] target is forced to the ground\n they cannot stand up for 1 turn",
    "Target suffers disadvantage on next attack they make",
    "Target is silenced, deafened, and blinded for 1 turn",
    "[Barkskin] Target's AC cannot be lower than 16, \n but gains vulnerability to fire and slashing",
    "[Boneskin] Target's AC cannot be lower than 16, \n but gains vulnerability to radiant and bludgeoning",
    "[Gelatinous form] Target speed becomes 15, \n can occupy space of others, immune to prone and poison and acid, \n resist all physical, vuln to cold, thunder, electric",
    "[Immobilize] Target loses turn, as if hit by hold person/hold monster for 1 turn",
    "[Sleep] Target falls asleep. Getting hit will wake.",
    "[Polymorph]: target rolls on the random polymorph table",
    "Crit Debuff! Player chooses to project a status effect on them, \n e.g polymorph, sleep, or restrain among others at DM discretion"
]

# expanded to allow choice on crit miss or crit hit
#  Based off rolling 2d8s
element_dict = {
    2: "(target's resistant element)", 
    3: "fire",
    4: "force",
    5: "lightning",
    6: "poison",
    7: "psychic",
    8: "thunder",
    9: "piercing",
    10: "slashing",
    11: "bludgeoning",
    12: "acid",
    13: "necrotic",
    14: "radiant",
    15: "cold",
    16: "player's choice"
}

def roll_2d8_and_1d6():
    first_d8 = random.randint(1, 8)
    second_d8 = random.randint(1, 8)
    damage_d6 = random.randint(1, 6)
    # Add damage together for total
    damage_total = (first_d8 + second_d8 + damage_d6)
    dam_roll_string = f"{first_d8} + {second_d8} + {damage_d6} = {damage_total}"
    return [dam_roll_string, damage_total]

def roll_2d8_for_element():
    first_d8 = random.randint(1, 8)
    second_d8 = random.randint(1, 8)
    # Add damage together for total
    result_total = (first_d8 + second_d8)
    # print(f"{element_dict[result_total]} rolled for Element type --> {first_d8} + {second_d8} = [{result_total}]")
    return element_dict[result_total]

def declare_damage_or_debuff():
        # establish an input loop to declare the type of cast it is, damage or debuff
    dam_or_debuff_input_loop_is_active = True
    while dam_or_debuff_input_loop_is_active:
        intention_input_string = input("Is the cast for damage? [y] \n\t --- If sacting debuff, submit [n]")
        if intention_input_string == "y":
            print("--- Damage Selected")
            dam_or_debuff_input_loop_is_active = False
            intention_inversion_roll =  random.randint(1, 8)
            if intention_inversion_roll == 1:
                print("... but chaos inverts it to a Debuff instead!")
                return ("debuff")
            else:
                print(f"Passed the inversion check 1 < [{intention_inversion_roll}]")
                return ("damage")
            
        elif intention_input_string == "n":
            print("--- Debuff Selected")
            dam_or_debuff_input_loop_is_active = False
            intention_inversion_roll =  random.randint(1, 8)
            if intention_inversion_roll == 1:
                print("... but chaos inverts it into Damage instead!")
                return ("damage")
            else:
                print(f"Passed the inversion check 1 < [{intention_inversion_roll}]")
                return ("debuff")
        else:
            print("unexpected input encountered... try again --> ")

# True or false expected result
#  --> Did enemy succeed on saving roll?
def roll_chaos_effect_spell_save():
    rand_stat_for_debuff_save = random.choice(core_stats_list)
    target_resist = input(f"What is the target's modifier for {rand_stat_for_debuff_save} saves?\n\t>> ")
    resistance_integer = int(target_resist)
#  instead of adding a spell attack modifier, roll 1d6 for the buff amount
    # for a lvl 1 spell, average should be around DC 14 for players, so 11 base plus 1d6 is 14.5 average DC with the 1d6 chaos die in place of a flat modifier
    player_chaos_buff = random.randint(1, 6)
    spell_DC_base = 11
    total_spell_DC = (player_chaos_buff + spell_DC_base)
    print(f"1d6 [{player_chaos_buff}] + base {spell_DC_base} == {total_spell_DC} DC for chaos bolt effect")
# roll for the enemy's save
    enemy_save_roll = random.randint(1, 20)
    enemy_save_total = enemy_save_roll + resistance_integer
    print(f"Enemy rolled [{enemy_save_roll}] + {resistance_integer} ---> For a {enemy_save_total} {rand_stat_for_debuff_save} save")
    # if enemy saves against spell, only deal 3d4 damage instead of effect
    # victim must EXCEED the spell save to resist it, tie goes to spellcaster
    if enemy_save_total > total_spell_DC:
        print(f"{rand_stat_for_debuff_save} save {enemy_save_total} > DC {total_spell_DC} : The enemy resisted the effect! :(")
        return True
    else:
        print(f"{rand_stat_for_debuff_save} save {enemy_save_total} < DC {total_spell_DC} : The spell inflicted the effect!")
        return False

def cast_chaos_polymorph():
    #choose a random form to turn them into if they get morphed
    chosen_form = random.choice(rand_polymorph_list_CR_1_enemy)
    
    wis_string = input("Input target's Wisdom save modifier > ")
    wis_score = int(wis_string)

    # Base wis save is 10
    # - Instead of adding proficiency + modifier, chaos uses 1d8; more likely to take effect, but less controlled 
    dc_base = 10
    dc_increase_by_1d8 = random.randint(1, 8)
    polymorph_dc = dc_base + dc_increase_by_1d8

    enemy_save_roll = random.randint(1,20)
    total_enemy_save = (enemy_save_roll + wis_score)
    print(f"[{enemy_save_roll}] + wis {wis_score} = {total_enemy_save}")

    if enemy_save_roll == 20:
        print(f"Chaos backfires! The caster is turned into \n {chosen_form}")
#  must exceed DC to not get polymorphed
    elif total_enemy_save > polymorph_dc:
        print(f"They were going to be turned into \n {chosen_form} \n but the enemy resisted the polymorph attempt! ")
    else:
        # enemy failed
        print(f"The chaos energy turns the target into.. \n {chosen_form}")

def roll_for_critical_debuff_spawn(total_first_3d4_dam, elemental_dam_type, rand_effect): 
    second_debuff_resonance = random.randint(19, 20)
    # get a second debuff:
    second_rand_effect = random.choice(chaos_debuff_list)
    is_second_debuff_crit = False
#  if 2 crits are in a row, deal max damage, so 12 automatically, if the debuff does damage
    if second_debuff_resonance == 20:
        is_second_debuff_crit = True
        print("[20] DOUBLE CRIT! A second debuff is inflicted with max damage!")
    else:
        print(f"[{second_debuff_resonance}] rolled for second debuff resonance (no crit. triggered)")
    if "polymorph" in second_rand_effect:
        if total_first_3d4_dam > 0:
            print(f"\t --- The first effect deals {total_first_3d4_dam} {elemental_dam_type} damage\n and launches a Chaotic Polymorph!")
        else:
            print(f"\t --- The first effect's {elemental_dam_type} energy causes --> {rand_effect} \n -- The chaos energy continues and...")
        print("- [!] Chaotic polymorph occurs!")
        cast_chaos_polymorph()
    elif "damage" in second_rand_effect: 
        print(f"Damaging effect detected... \n{second_rand_effect}")
        # automatically give max (12) damage for a second crit
        if is_second_debuff_crit:
            total_second_3d4_dam = 12
        else:
            second_d4_a = random.randint(1,4)
            second_d4_b = random.randint(1,4)
            second_d4_c = random.randint(1,4)
            total_second_3d4_dam = second_d4_a + second_d4_b + second_d4_c 
        # roll 2d8 for the random element table
        element2_d8_a = random.randint(1,8)
        element2_d8_b = random.randint(1,8)
        element2_selection_num = element2_d8_a + element2_d8_b
        elemental_dam_type2 = element_dict[element2_selection_num]
        # need to handle output strings for both cases if the first effect did damage, or only did a pure effect without damage
        if total_first_3d4_dam > 0:
            print(f"\t --- The first effect deals {total_first_3d4_dam} {elemental_dam_type} damage\n and causes {rand_effect}")
        else:
            print(f"\t --- The first effect's {elemental_dam_type} energy causes --> {rand_effect}")
        print(f"[+crit Damage Debuff] Second debuff deals {total_second_3d4_dam} {elemental_dam_type2} damage and inflicts ... \n {second_rand_effect}")
    else:
        if total_first_3d4_dam > 0:
            print(f"\t --- The first effect deals {total_first_3d4_dam} {elemental_dam_type} damage\n and causes {rand_effect}")
        else:
            print(f"\t --- The first effect's {elemental_dam_type} energy causes --> {rand_effect}")
        print(f"[+crit Pure Debuff] The second debuff summons {elemental_dam_type2} energy to inflict --> {second_rand_effect}")
    #  a third debuff cannot occur, balance-wise, so it's not a loop

def cast_debuff_spell():
    # Set boolean for crit, initially false
    is_crit_debuff = False

    # get primary element
    element_d8_a = random.randint(1,8)
    element_d8_b = random.randint(1,8)
    element_selection_num = element_d8_a + element_d8_b
    elemental_dam_type = element_dict[element_selection_num]

    # get random effect
    rand_effect = random.choice(chaos_debuff_list)

    # roll enemy save, True means the player won the contest, False means they did not
    did_enemy_succeed_on_save = roll_chaos_effect_spell_save()
    if did_enemy_succeed_on_save:
    #  If the keyword "damage" is in the effect description, it deals 3d4 damage in addition to an effect
        if "damage" in rand_effect:
            mulligan_d4_a = random.randint(1,4)
            mulligan_d4_b = random.randint(1,4)
            mulligan_d4_c = random.randint(1,4)
            mulligan_total = (mulligan_d4_a + mulligan_d4_b + mulligan_d4_c)
                    # log the effect resisted for diagnostics. If it hits, the output string at the end will list the effects.
            print(f"Effect evaded -> {rand_effect}")
            print(f" [!] --- The enemy saved against the effect, but still takes [{mulligan_total}] {elemental_dam_type} damage!")
        else:   
            print(f"The enemy evaded the {elemental_dam_type} energy \n effect evaded --> {rand_effect}")
    else: 
    #  check for critical, which will spawn a second debuff
        debuff_resonance = random.randint(19, 20)
        if debuff_resonance == 20:
            print("[20] Critical debuff! Second debuff triggered")
            is_crit_debuff = True
        else:
            print(f"[{debuff_resonance}] Rolled for resonance (no double-debuff triggered)")
        if "damage" in rand_effect:
            # print(f"Damaging effect detected... \n{rand_effect}")
            d4_a = random.randint(1,4)
            d4_b = random.randint(1,4)
            d4_c = random.randint(1,4)
            total_first_3d4_dam = d4_a + d4_b + d4_c 
        # double the damage, then roll second effect and check for double crit
            if is_crit_debuff:
                # double the damage from the first effect
                # multiplying it by two appears easier to read, IMO... getting alt. opinions by having multiple examples of the same thing for 2x-ing the damage
                total_first_3d4_dam = (total_first_3d4_dam * 2)
                roll_for_critical_debuff_spawn(total_first_3d4_dam, elemental_dam_type, rand_effect)
            else: 
                print(f"Deal {total_first_3d4_dam} {elemental_dam_type} damage!\n inflict effect: {rand_effect}")
        else:
            print(f"inflict pure status effect: {rand_effect}")
            # In the case that there's a critical debuff, so a second one is spawned, but no initial damage needs to be rolled for the first effect...
            if is_crit_debuff:
                roll_for_critical_debuff_spawn(0, elemental_dam_type, rand_effect)
                

def make_spell_attack_roll():
    # prep the element, which will be reported regardless of hit or miss for flavor
    element_type = roll_2d8_for_element()
    target_AC_str = input("What is target's AC?")
    target_AC = int(target_AC_str)
    spell_attack_string = input("What is caster's spell attack modifier?")
    spell_attack_modifier = int(spell_attack_string)
    is_critical = False
    spell_atk_roll = random.randint(1, 20)
    total_acc = spell_atk_roll + spell_attack_modifier
    print(f" -- rolled {spell_atk_roll} + atkMod {spell_attack_modifier} = [{total_acc}] to hit")
    # "meet or exceed" AC in order to hit, thus ties always hit
    if spell_atk_roll == 20:
    # Critical hit mini-banner
        print("----!!!-----\n [!] CRITICAL HIT for casting chaos bolt! \n ----!!!-----")
        is_critical = True
    if total_acc >= target_AC: 
        print(f"{total_acc} HITS target [{target_AC} AC]")
        dam_result_list = roll_2d8_and_1d6()
        dam_result_string = dam_result_list[0]
        dam_total_int = dam_result_list[1]
        if is_critical:
        # adding the total to itself is another way of multiplying the result by 2 for a critical to double the damage
            dam_total_int += dam_total_int
        print(f"{dam_result_string}\n\t {dam_total_int} points of {element_type} damage <---")
        return("hit")
    else:
        print(f"the {element_type} energy MISSES ({total_acc} atk < {target_AC} AC")
        return("miss")

def cast_chaos_bolt():
    description_string1 = "A shifting mass of chaotic energy forms over the spellcasting focus."

    dam_or_debuff_string = declare_damage_or_debuff()
    if dam_or_debuff_string == "damage":
        make_spell_attack_roll()
    else:
        cast_debuff_spell()


    # hit_or_miss = make_spell_attack_roll(spell_attack_modifier, target_AC)
    # if hit_or_miss == "hit":
    #     continue_chaos_coin_flip = random.randint(1,2)
    #     num_chaos_jumps = 0
    #     # loop until the chaos jumps do so no more
    #     while continue_chaos_coin_flip == 2:
    #         num_chaos_jumps += 1
    #         next_target_AC = input("what is the next target's AC?")
    #         subsequent_hit_string = make_spell_attack_roll(spell_attack_modifier, next_target_AC=10)
    #         continue_chaos_coin_flip = random.randint(1,2)
    # handle attack
    # if num_chaos_jumps > 0:
        # print(f"chaos {jumped num_chaos_jumps} times!")
    # else:
        # print("The chaos was contained to a single target")

exit_string = "potato"
while exit_string != "x":
    # caster_modifier = input("Input caster's spell attack modifier: ")
    # target_AC = input("Input target's AC: ")
    cast_chaos_bolt()
    exit_string = input("\t>> enter to continue or [x] to quit : ")

print("Ending chaotic program...")

#  CHAOS CHANCE for EXTRA: suffocating and silenced, blinded, thunder and deafened
# 25% chance to jump would be 2d4. 0.5 dam average lower than 1d10 for eldritch blast cantrip, which cannot jump...
#  EXTRA: high level do multiple chaos bursts like for eldtrich blast
# as a 2 d4 + cha cantrip, if it jumps, it will hit an ally if no other target is available, but then can jump back
# to hit a primary target. The uncontrolled nature forces it to attack a living thing UNLESS the primary target is an object first.
# alt

# Extra: item ALWAYS allows the chaos bolt's type to be chosen