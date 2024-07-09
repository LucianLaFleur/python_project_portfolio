

wild_magic_dict = {
# event number : description, flavor, tags
1: ["Roll twice, and initiate two effects, ignoring multi-effects like this one", "flavorless", ["special", "approved"]],
2: ["magic eyeball -->", "flavorless", ["unapproved"]],
# 3: ["A totem pole with scary faces appears, (appearance, obstruction, effect)", "flavorless", ["interaction", "unapproved"]],
# 4: ["Your fingertips tingle with power "]
# distracting DC IMAGE inflicts [gather, disadv. ]
# you move random direction, up to 20 ft, a single target you can see also moves the same amount in the same direction

}

finger_power_arr = [
    "disintegration 6d10", "petrify into stone", "petrify, marble with veins of gold, 50gp x CR"
]

#           CR      AC      HP     Atk+    DPR      DC     Save
# "0": [     0,     12,     3,      2,      1,      9,      1],
#  "1/8": [0.125,    12,     9,      3,      3,      10,     2],
#  "1/4": [0.25,     13,     15,     3,      5,      10,     2],
#  "1/2":[    0.5,   13,     24,     4,      8,      11,     3],
#  "1":  [      1,   13,     30,     4,      10,     11,     3],
#  "2": [       2,   13,     45,     5,      15,     12,     4],
#  "3": [       3,   14,     60,     5,      20,     12,     4],
#  "4": [       4,   14,     75,     6,      25,     13,     5],
#  "5": [       5,   14,     90,     6,      30,     13,     5],
#  "6": [       6,   15,     105,    7,      35,     14,     6],
#  "7": [       7,   15,     120,    7,      40,     14,     6],
#  "8": [       8,   15,     135,    8,      45,     15,     7],
#  "9": [       9,   16,     150,    8,      50,     15,     7],
#  "10":[      10,   16,     165,    9,      55,     16,     8],
#  "11":[      11,   16,     180,    9,      60,     16,     8],
#  "12":[      12,   17,     195,    10,     65,     17,     9],
#  "13":[      13,   17,     210,    10,     70,     17,     9],
#  "14":[      14,   17,     225,    11,     75,     18,     10],
#  "15":[      15,   18,     240,    11,     80,     18,     10],
#  "16":[      16,   18,     255,    12,     85,     19,     11],
#  "17":[      17,   18,     270,    12,     90,     19,     11],
#  "18":[      18,   19,     285,    13,     95,     20,     12],
#  "19":[      19,   19,     300,    13,    100,     20,     12],
#  "20":[      20,   19,     315,    14,    105,     21,     13]

cr_dice = {
#  CR :    full DAM,  halfDAM, atk+, DC
    1 : [["3d6", 0], ["2d4", 1], 4, 11],
    #  NEEDS EXPANSION  WITH CALCULATOR; NEEDS EFFECTS HALVING FOR SECOND DPR NUM
}

eye_appearances = [
    "slit eye",
    "goat-eye",
    "bloodshot eye",
    "swirling pupil eye",
    "skulls-for-pupils eye",
    "bright green eye",
    "bright blue eye",
    "clouded-over blind eye"
]

totem_appearances = [
    "dragon",
    "scorpion",
    "geometric carved crystals",
    "ancient wood with faint swirl-designs",
    "wolf-carving",
    "screaming eagle",
    "skeleton",
    "dwarf-face with war-paint",
    "tree made of hands",
    "insect heads (beetle, mantis, spider)"
]

rand_effect_type = [
    # damage done twice so 50% for a damaging totem
    "damage",
    "damage"
    # "buff",
    # "debuff"
]

high_debuffs = [
    "immobilized- numb/chrono-locked", "silenced/deafened", "blinded", "restrained", "disadv. to defend", "adv. to hit it", "disadv. on saves/checks", 
    "flat-prone (next action on ground, cannot move 1 turn)", "misdirected (1d10 random movement NYI)", "You know their next move and automatically dodge/save against it"
]

buffs = [
    "Add HALF_CR to checks for 1 minute", "Add proficiency modifier on top of normal to-hit for 1 minute",
    "Add 1d6 + proficiency modifier to AC of next attack that would hit", "heal for HALF_CR", "gain extra action on next turn", "next attack that hits deals double-damage", "next attack moves enemy up to 20ft in chosen direction", "gain advantage on next attack / next save for enemy is made with disadvantage", "gain spider-climb and +10ft movement for 1 minute", "Vertical jump becomes 15 and horizontal becomes 30; can jump using movement distance",
]

obstruction_list = [
    "covered in spiderwebs (5hp, burnable)", "with vines crawling up it, (5hp, burnable)", "with handles on the sides (no obstruction)", "(investigation check DC) hand-holds in the carving",
    "(arcana check DC) arcane inscription", "(int check DC) a series of WOOD and STONEWORK levers", "(sleight of hand DC) a crystal shard sticks out conspicuously, jamming it", 
    "(Athletics DC + 2) a mechanical crank is rusted in place"
]

# for x in obstruction_list:
#     if "DC" in x:
#         print(f"DC keyword hit in item : \n\t{x}")

targets_list = [
    "chosen target, effect unknown", "self", "random ally", "random enemy", "chosen target, effect known"
]

all_aoe_types = [
    "15ft cone", "30ft line", "20ft radius", "15ft cube", "30ft range, hit 1, chain to nearest in 20ft", "60ft single target", "20ft and 15ft radius", "lingering 15ft cube hazard"
]

all_dam_types = ["physical- blunt", "physical - piercing", "physical - slashing", "force", "psychic", "thunder", "electric", "poison", "fire",  
"cold", "radiant", "necrotic", "magic - piercing", "magic - slash"]
# magic - blunt excluded because force is already there

rand_directions = ["in place", "N", "NE", "E", "SE", "S", "SW", "W", "NW", "chosen direction"]

# make a list from a range 1 to length of wild_magic_dict, adding 1 because ranged are not inclusive
valid_range_list = list(range(1,(len(wild_magic_dict)+1)))
# print(f"Checking valid range : num of dict items detected = {valid_range_list}")