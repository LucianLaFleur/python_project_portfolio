import random
rand_polymorph_list_CR_1_enemy = [
    "slug 4AC, 1HP, 5climb",
    "housefly 14AC, 1HP, 60fly",
    "wasp 14AC, 1HP, 1d4 (4 atk), 60fly",
    "glowing scarab 11AC, 6HP, +3 hit 1 pierce, 30climb",
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

# simple loop for testing
myvar1 = True
while myvar1:
    cast_chaos_polymorph()
    user_input = input("enter to continue, or x to quit")
    if user_input == "x":
        myvar1 = False