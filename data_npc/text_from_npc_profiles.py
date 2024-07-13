from bs4 import BeautifulSoup as bs
import requests
import time
import random

# ---- current limit at 2900, so it shouldn't trip 3k ----------

ordered_name_arr = []
# Reads from the list of NPC names, duplicate entries removed (from existing on the NPC source list)
with open("dupes_removed_npc_name_list.txt", "r", encoding="UTF-8") as npc_name_file:
    dirty_arr = npc_name_file.readlines()
    for x in dirty_arr:
        ordered_name_arr.append(x.strip())

url = "https://genshin-impact.fandom.com/wiki/"

named_npc_master_list = []
for name in ordered_name_arr:
    individual_sub_list = []
    # Append the url + name as the 0 idx item
    individual_sub_list.append(url + name)
    # remove the %22 marking quotes in the name if it's found; cleans up file names
    if "%22" in name:
       name = name.replace("%22", "")
    elif '"' in name:
        name = name.replace('"', '')
    # Append the clean name itself as 1 idx item   
    individual_sub_list.append(name)   
    
        # output will be = [name1, url/name1]
            # this will make the named_npc_master_list a list with several sub-lists nested inside at a depth of 1
    named_npc_master_list.append(individual_sub_list)

# PRESERVED for-loops testing randomization --> Testing helped me not accidentally run and re-run the entire lists multiple times
        #  when I was calling the entire set of 1000+ characters instead of the sliced test subset of a few
        # sample_arr_slice = ordered_name_arr[61:69] 
        # ...
# for x in sample_arr_slice:
#     print(x)
# print(f"-" *34)
# print("RANDOMIZING")
# print(f"-" *34)
# random.shuffle(sample_arr_slice)
# for y in sample_arr_slice:
#     print(y)
# print(f"-" *34)
# input("pausing.... 0013")
# print(test_urls)


# ! PRESERVED, 
    #  Randomization not needed here ebcause the remove_dupe_names already randomizes order by converting to a set then a list, 
        # this also removed duplicates so we're never looking at the same article twice, saving on efficiency.
# randomize the array, so looking in alphabetical order doesn't look suspicious like a spider
# random.shuffle(named_npc_master_list)

print(f"{len(named_npc_master_list)} names detected, ready to process?")
input(" >> ")

#  OLD VERSION PRESERVED:
    #  --- tested on an array of known target names to see if the pattern works for special characters in the names

# # test_names = ["I._Ivanovna_N.", "Dr._Livingstone", "%22Kichiboushi%22"]

# url = "https://genshin-impact.fandom.com/wiki/"

# test_urls = []
# clean_names_for_text_files = []
# for name in test_names:
#     test_urls.append(url + name)
#     # remove the %22 marking quotes in the name if it's found; cleans up file names
#     if "%22" in name:
#        name = name.replace("%22", "")
#     # otherwise, no change needs to be made and can be added straight
#     clean_names_for_text_files.append(name)

file_name_base = "_word_salad.txt"
# --- Exceptional characters, needing checking from how UTF-8 stores them in .txt file
# https://genshin-impact.fandom.com/wiki/I._Ivanovna_N.
# https://genshin-impact.fandom.com/wiki/Dr._Livingstone
# https://genshin-impact.fandom.com/wiki/%22Kichiboushi%22

# Function made for varying the sleep time, so it's not suspiciously consistent times between requests
def get_float_for_sleep():
    # float will be between 5.1 and 8.9 seconds, reasonable enough throttling
    # ...
# first, build up the ranges
    seconds = range(5,9)
    tenths_of_seconds = range(1,10)
# Randomly select an item from the range
    unconverted_int = random.choice(tenths_of_seconds)
    # divide by 10 to put in the tenths place
    converted_tenth = float(unconverted_int/10)
    whole_seconds = float(random.choice(seconds))
    result_float = whole_seconds + converted_tenth
        #  e.g --> 3.4
    return result_float

# Use the url constructed for the given npc's page
def fetch_npc_word_salad(url):
    headers = {"Connection":"keep-alive",'User-Agent': 'Mozilla/5.0'}
    html_page = requests.get(url, headers=headers)
    soup = bs(html_page.text, "html.parser")
    #  the text is found in the following content item
    npc_text_content = soup.find('div', id='mw-content-text').get_text()
    return npc_text_content

#  Process execution -----------------------------------------------------------------

wierd_list = []
name_idx = 0
for sub_arr in named_npc_master_list:
    if name_idx > 3000:
        input("Should not be over 3000 names. Something fishy is going on...\n PAUSED: check code before continuing")
    print(f"Writing file for : {sub_arr[1]}")
    salad = fetch_npc_word_salad(sub_arr[0])
#   use the clean name list for naming the output textfiles -> Should remove %22 from quotes if they appear
        #  further cleaning may be needed if bad data appears still for other characters
        # all are prefixed with the directory for the npc text for easy identificaiton
    try:
        with open("./npc_text/" + sub_arr[1] + file_name_base, "w", encoding="UTF-8") as outfile:
            outfile.write(salad)
    except:
        print(f"weirdness occurred with {sub_arr[1]} at index {str(name_idx)}")
        wierd_list.append(sub_arr[1])
        try:
            with open("./npc_text/" + str(name_idx) + file_name_base, "w", encoding="UTF-8") as outfile:
                outfile.write(salad)
        except:
            print("double weirdness found... no action taken")
    # increment the index to move to the next person, then sleep to not overwhelm the site
    name_idx += 1
    varying_sleepy_float = get_float_for_sleep()
    print(f"\t #{str(name_idx)} done, sleeping for --> {str(varying_sleepy_float)}")
    time.sleep(varying_sleepy_float)

print("All items in target array scanned and files created! \n End of program!")

# print(f"{file_name} created!")
# print(f"{space_items} items with spaces corrected")
