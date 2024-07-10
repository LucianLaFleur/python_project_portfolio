from bs4 import BeautifulSoup as bs
import requests
import time

# structure:
# https://genshin-impact.fandom.com/wiki/Annette
# https://genshin-impact.fandom.com/wiki/NPC/List

npc_name_arr = []
with open("genshin_npc_name_list.txt", "r", encoding="UTF-8") as npc_name_file:
    dirty_arr = npc_name_file.readlines()
    for x in dirty_arr:
        npc_name_arr.append(x.strip())

url = "https://genshin-impact.fandom.com/wiki/"

test_urls = []
clean_names_for_text_files = []
for name in npc_name_arr[132:136]:
    test_urls.append(url + name)
    # remove the %22 marking quotes in the name if it's found; cleans up file names
    if "%22" in name:
       name = name.replace("%22", "")
    # otherwise, no change needs to be made and can be added straight
    clean_names_for_text_files.append(name)

# print(test_urls)
# input(" >> ")

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

# https://genshin-impact.fandom.com/wiki/I._Ivanovna_N.
# https://genshin-impact.fandom.com/wiki/Dr._Livingstone
# https://genshin-impact.fandom.com/wiki/%22Kichiboushi%22

def fetch_npc_word_salad():
    # names_list = []
    # init the names list that we ultimately want for the output
    headers = {"Connection":"keep-alive",'User-Agent': 'Mozilla/5.0'}
    html_page = requests.get(url, headers=headers)
    soup = bs(html_page.text, "html.parser")
    npc_text_content = soup.find('div', id='mw-content-text').get_text()
    return npc_text_content

#  Process execution -----------------------------------------------------------------
# 
name_idx = 0
for url in test_urls:
    if name_idx > 3000:
        input("over 3000 names? Really? Something fishy is going on...\n check code before continuing")
    print(f"Writing file for : {clean_names_for_text_files[name_idx]}")
    salad = fetch_npc_word_salad()
#   use the clean name list for naming the output textfiles -> Should remove %22 from quotes if they appear
        #  further cleaning may be needed if bad data appears still for other characters
        # all are prefixed with the directory for the npc text for easy identificaiton
    with open("./npc_text/" + clean_names_for_text_files[name_idx] + file_name_base, "w", encoding="UTF-8") as outfile:
        outfile.write(salad)

    # increment the index to move to the next person, then sleep to not overwhelm the site
    name_idx += 1
    time.sleep(1)

print("and we're out!")
# # .... ummm...

# print(f"{file_name} created!")
# print(f"{space_items} items with spaces corrected")
