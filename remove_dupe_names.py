# ! Duplicate names were found in the npc name list, putting what should be under 3000 into over 5000 items.
#       removal of duplicate names from textfile needed...

ordered_name_arr = []
with open("genshin_npc_name_list.txt", "r", encoding="UTF-8") as npc_name_file:
    dirty_arr = npc_name_file.readlines()
    for x in dirty_arr:
        ordered_name_arr.append(x.strip())

# PRESERVED:---  Same logic, but clunky in an array iteration format...

# clean_arr = []
# for x in in_arr:
#     if x not in clean_arr:
#         clean_arr.append(x)

out_arr = list(set(ordered_name_arr))
# Sanity check to make sure it's less than the original number. 
# putting things into a set will change the ordering of the list, but we want that so we're not
    # suspiciously browsing in-order
print(len(out_arr))

with open("dupes_removed_npc_name_list.txt", "w", encoding="UTF-8") as npc_name_file:
    for name in out_arr:
        npc_name_file.write(name + "\n")