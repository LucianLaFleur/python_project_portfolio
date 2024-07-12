import random

# character_list = []
# with open("underscored_genshin_names.txt", "r", encoding="UTF-8") as character_name_file:
#     dirt_list = character_name_file.readlines()
#     for item in dirt_list:
#         character_list.append(item.strip())

# for x in character_list[12:18]:
#     print(x)

# character_list2 = random.shuffle(character_list)

# input("enter to randomize ... ")

# for y in character_list[12:18]:
#     print(y)


#  Randomize the seconds and tenths of seconds waited

seconds = range(1,7)
tenths_of_seconds = range(1,10)

#  for test purposes, just do the loop 8 times
for x in range(1,9):
    unconverted_int = random.choice(tenths_of_seconds)
    # divide by 10 to put in the tenths place
    converted_tenth = float(unconverted_int/10)
    whole_seconds = float(random.choice(seconds))
    result_float = whole_seconds + converted_tenth
    print(result_float)
