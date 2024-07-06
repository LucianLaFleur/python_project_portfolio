# Automation of chaos bolt, Rules-as Written, Xanthar's guide to Everything, DnD 5e
#  -- This is for educational purposes only, and I have no affiliations, nor do I profit from this.
# 1st level spell
import random
# 2d8 + 1d6 dam

# From "chaos bolt" description, oddly enough, it's in alphabetical order. Ignored physical-type damage sources, and electric, necrotic, radiant, are all omitted
element_from_d8 = {
    1: "acid",
    2: "cold",
    3: "fire",
    4: "force",
    5: "lightning",
    6: "poison",
    7: "psychic",
    8: "thunder"
}


# chaos_die_for_threshold = 8


def cast_chaos_bolt(spell_attack_modifier=0, target_AC=13):
    # d8 is the standard dice pair for the damage dice
    # Lowering this will lower overall damage, but make the coincidence more likely
    chaos_die_for_threshold = 8
    description_string1 = "A shifting mass of chaotic energy springs forth, rippling with a mixture of constantly-changing colors."
    is_critical = False
    # Roll d20 for atk
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
        first_d8 = random.randint(1, chaos_die_for_threshold)
        second_d8 = random.randint(1, chaos_die_for_threshold)
        damage_d6 = random.randint(1, 6)
    # Add together the damage dice for a total
        damage_total = (first_d8 + second_d8 + damage_d6)
    # Damage type determined by the first d8
        dam_type_str = f"{element_from_d8[first_d8]} damage"
    # Show the rolls and calculations, diagnostic
        print(f"[{first_d8} + {second_d8}] + {damage_d6} =\n\t MAIN Target takes {damage_total} {dam_type_str}<---")

    # Check for chaos-resonance: if the same number is on both d8's chaotic energy leaps to another target within 30 feet
    #  make a new attack roll against the new target and a new damage roll, which could cause a leap again
        while first_d8 == second_d8:
            print("[Chaotic Resonance]! Another burst of energy erupts!")
            # Roll again to make a separate attack
            spell_atk_roll = random.randint(1, 20)
            total_acc = spell_atk_roll + spell_attack_modifier
            print(f" -- rolled {spell_atk_roll} + atkMod {spell_attack_modifier} = [{total_acc}] to hit")
            if spell_atk_roll == 20:
            # Critical hit mini-banner
                print("----!!!-----\n [!] CRITICAL HIT for casting chaos bolt! \n ----!!!-----")
                is_critical = True
            first_d8 = random.randint(1, chaos_die_for_threshold)
            second_d8 = random.randint(1, chaos_die_for_threshold)
            damage_d6 = random.randint(1, 6)
            aux_damage_total = (first_d8 + second_d8 + damage_d6)
        # Damage type determined by the first d8
            dam_type_str = f"{element_from_d8[first_d8]} damage"
        # Show the rolls and calculations, diagnostic
            print(f"[{first_d8} + {second_d8}] + {damage_d6} =\n\t EXTRA TARGET takes {damage_total} {dam_type_str}<---")
    else:
        print(f"{total_acc} MISSES against [{target_AC} AC]")



exit_string = "potato"
while exit_string != "x":
    caster_modifier = input("Input caster's spell attack modifier: ")
    target_AC = input("Input target's AC: ")
    cast_chaos_bolt(4, 14)
    exit_string = input("\t>> enter to continue or [x] to quit : ")

print("Ending chaotic program...")

#  CHAOS CHANCE for EXTRA: suffocating and silenced, blinded, thunder and deafened
# 25% chance to jump would be 2d4. 0.5 dam average lower than 1d10 for eldritch blast cantrip, which cannot jump...
#  EXTRA: high level do multiple chaos bursts like for eldtrich blast
# as a 2 d4 + cha cantrip, if it jumps, it will hit an ally if no other target is available, but then can jump back
# to hit a primary target. The uncontrolled nature forces it to attack a living thing UNLESS the primary target is an object first.
# alt