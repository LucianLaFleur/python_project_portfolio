import random
# import the dictionary of effects listed in the wild_magic_dictionary file
from wild_magic_dictionary import *
import math

def handle_summoned_eyeball(given_CR):
    critical_check = random.randint(1, 20)
    is_critical = False
    if critical_check == 20:
        is_critical == True
        print("[+ CRIT!] target is caster's choice")    
    eye_appearance = random.choice(eye_appearances)
    print(f"A spectral beholder appears above the casting focus; it points a stalk with\n\t a {eye_appearance}.")
    target = random.choice(targets_list)
    aoe_type = random.choice(all_aoe_types)
    effect_type = random.choice(rand_effect_type)
    if effect_type == "damage":
        acc_and_dam = roll_for_wild_mag_atk(cr_dice[given_CR][0], given_CR)
        dam_type = random.choice(all_dam_types)
        print(f"target: {target}\n aoe: {aoe_type}\n detail: Ranged magic [ATTACK] for {acc_and_dam[0]} to hit, {acc_and_dam[1]} {dam_type} damage")
        if is_critical:
           print("DOUBLE the damage because of crit, auto-hit")
#    buff and debuff should be already balanced for auto-hitting
    elif effect_type == "buff":
        buff_type = random.choice(buffs)
        print(f"target: {target}\n aoe: {aoe_type}\n detail: [BUFF] apply {buff_type}")
        if is_critical:
           print("DOUBLE the buff-effect because of crit")
    elif effect_type == "debuff":
        debuff_type = random.choice(high_debuffs)
        print(f"target: {target}\n aoe: {aoe_type}\n detail: [DE-BUFF] inflict {debuff_type}")
        if is_critical:
           print("DOUBLE the debuff duration because of crit")
    else:
        print("unexpected effect roll, check code")

def process_wild_roll(wild_roll, given_CR):
    # if wild_roll == 2:
    handle_summoned_eyeball(given_CR)


def roll_for_wild_mag_atk(cr_dam_list, given_CR):
    # instead of getting flat accuracy, the accuracy will be normalized around the CR accuracy value (plus to attack) at cr_dice[given_CR][2] in the dictionary
    # this will give an "average" bonus around what it "should" be, with more variability than just a plain d20 roll.
    # this means more powerful magic will become more powerfully unpredictable
    atk_die_1 = random.randint(1, cr_dice[given_CR][2])
    # subtract 1, because dice averages are always + .5 for starting at 1, like 1d6 = 3.5 avg, or 1d4 = 2.5 avg
    atk_die_2 = random.randint(1, cr_dice[given_CR][2] - 1)
    atk_d20 = random.randint(1, 20)
    atk_val = (atk_die_1 + atk_die_2 + atk_d20)
    print(f"ACC [{atk_val}] - For Wild Magic Accuracy; rolled {atk_die_1} + {atk_die_2} + {atk_d20}")

    dice_string = cr_dam_list[0]
    # adds a flat number to keep DPR number balanced outside of what dice rolls offer
    additional_amount = cr_dam_list[1]
    print(f"Rolling {dice_string} plus {additional_amount}:")
    # split apart the string at the "d" to get the # of dice and die type (e.g. 6 =  six-sided)
    dice_list = dice_string.split("d")
    #   ex. ["3", "6"]
    # Need to conver string to integer
    num_of_dice = int(dice_list[0])
    type_of_dice = int(dice_list[1])
    total_dam_sum = 0 + additional_amount

    for die in range(1, (num_of_dice+1)):
        die_result = random.randint(1, type_of_dice)
        total_dam_sum += die_result
        print(f"Roll {die} d{type_of_dice} --> {die_result}")

    print(f"DAM Total ==> {total_dam_sum}")
    # total sum is the total 
    return [atk_val, total_dam_sum]

# ------------------ Process execution -----------------------------------------------------

#  NYI manual input for monster CR
# given_CR = input("Enter the CR# for caster")
given_CR = 1

looper_var = True
while looper_var == True:
    # print(cr_dice[given_CR][0]) # Diagnostic...
    rolled_num = random.choice(valid_range_list)
    print(f"Rolled {rolled_num} : \n {wild_magic_dict[rolled_num][0]}")
    process_wild_roll(rolled_num, given_CR)
    ender_input = input("Enter to continue, x to exit: ")
    if ender_input == "x":
        looper_var = False

print("end of program")


# while True:
#     randitem = random.choice(lines)
#     print(randitem)
#     lines.remove(randitem)
#     user_input = input("continue?")
#     if user_input == "x":
#         break