# CLEARLY MARKED AS HOMEBREW
#  Based on Xanthar's guide to Everything, DnD 5e -- This is for educational purposes only, and I have no affiliations, nor do I profit from this.
# ---
#  Difference log : 1) Higher chance for chaos-jumping (12.5% --> 33 %)
#                   12.5% chance on 2d8, which means only once out of every 8 casts of a lvl1 spell... not likely at all.
#  NYI              Exchanged for raw 50% chance of chaining (since separate attack rolls are needed, it's more fair and more engaging; should be easier to chain enemies who you got advantage on, encouraging tactics)
#                   roll 1d6, on 5 or 6 jump (instead of the 2d8 having to align)
#                   2) Chaotic variance: instead of 8 possible outcomes, 15 possiblilities exist for damage types                  
#                   3) jumping energy prioritizes living target > matching (fire burns, electric conducts in water, etc.) > destructable target (rope, wall, door) > doing nothing
#                       This priority must be taken in consideration when looking at the battlemap (positioning cannot be automated via CLI)
#                   4) Can declare intention to cast in damage mode or debuff mode; 12.5% chance (1/8) that the opposite mode will be chosen instead
# ---
import random

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
    "[Opening] Element hits for half damage, but next damage taken is doubled",
    "[Sunder] Element hits for half damage, next attack made on target is with advantage",
    "[Restrain] Element hits for half damage, target is restrained for 1 turn",
    "[slow] element hits for half damage, movement reduced by half",
    "Element hits for half damage, then disable/drop weapon if they have one, else, no effect.",
    "Element hits for half damage, target blinded 1 turn", 
    "Element hits for half damage, target deafened and silenced for 1 turn",
    "[Flat-prone] target is knocked on ground, cannot stand up for 1 turn",
    "Target suffers disadvantage on next attack they make",
    "Target is silenced, deafened, and blinded for 1 turn",
    "[Barkskin] Target's AC cannot be lower than 16, but gains vulnerability to fire and slashing",
    "[Boneskin] Target's AC cannot be lower than 16, but gains vulnerability to radiant and bludgeoning",
    "[Gelatinous form] Target speed becomes 15, can occupy space of others, immune to prone and poison and acid, resist all physical, vuln to cold, thunder, electric",
    "[Immobilize] Target loses turn, as if hit by hold person/hold monster for 1 turn",
    "[Sleep] Target falls asleep. Taking damage will wake.",
    "[Polymorph]: target rolls on the random polymorph table, becoming the target creature, damage carried over once HP from the form is depleted"
]

# expanded to allow choice on crit miss or crit hit
#  Based off rolling 2d8s
element_dict = {
    2: "target's resistance, if target's vulnerability, else player's choice", 
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
    print(f"{element_dict[result_total]} rolled for Element type --> {first_d8} + {second_d8} = [{result_total}]")
    return element_dict[result_total]

def declare_damage_or_debuff():
        # establish an input loop to declare the type of cast it is, damage or debuff
    dam_or_debuff_input_loop_is_active = True
    while dam_or_debuff_input_loop_is_active:
        intention_input_string = input("Is the cast for damage? [y] If debuff, submit [n]")
        if intention_input_string:
            print("--- Damage Selected")
            dam_or_debuff_input_loop_is_active = False
            intention_inversion_roll =  random.randint(1, 8)
            if intention_inversion_roll == 1:
                print("... but chaos inverts it to a Debuff instead!")
                return ("debuff")
            else:
                print(f"Passed the inversion check 1 < [{intention_inversion_roll}]")
                return ("damage")
            
        elif intention_input_string:
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

def make_spell_attack_roll(spell_attack_modifier, target_AC):
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
        element_type = roll_2d8_for_element()
        if is_critical:
        # adding the total to itself is another way of multiplying the result by 2 for a critical to double the damage
            dam_total_int += dam_total_int
        print(f"{dam_result_string}\n\t {dam_total_int} points of {element_type} damage <---")
        return("hit")
    else:
        print(f"{total_acc} MISSES against [{target_AC} AC]")
        return("miss")

def cast_chaos_bolt(spell_attack_modifier=0, target_AC=13):
    description_string1 = "A shifting mass of chaotic energy forms over the spellcasting focus."

    dam_or_debuff_string = declare_damage_or_debuff()

    # MANAGE LATER
    chance_for_chaos_resonance = random.randint(1,2)
        make_spell_attack_roll(spell_attack_modifier, target_AC)
    
    # check for atk critical

    

exit_string = "potato"
while exit_string != "x":
    # caster_modifier = input("Input caster's spell attack modifier: ")
    # target_AC = input("Input target's AC: ")
    # cast_chaos_bolt(4, 14)
    exit_string = input("\t>> enter to continue or [x] to quit : ")

print("Ending chaotic program...")

#  CHAOS CHANCE for EXTRA: suffocating and silenced, blinded, thunder and deafened
# 25% chance to jump would be 2d4. 0.5 dam average lower than 1d10 for eldritch blast cantrip, which cannot jump...
#  EXTRA: high level do multiple chaos bursts like for eldtrich blast
# as a 2 d4 + cha cantrip, if it jumps, it will hit an ally if no other target is available, but then can jump back
# to hit a primary target. The uncontrolled nature forces it to attack a living thing UNLESS the primary target is an object first.
# alt

# Extra: item ALWAYS allows the chaos bolt's type to be chosen