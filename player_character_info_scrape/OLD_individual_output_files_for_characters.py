from bs4 import BeautifulSoup as bs
import requests
import time

# structure:
# https://genshin-impact.fandom.com/wiki/name

# Lore
# https://genshin-impact.fandom.com/wiki/Kaveh/Lore


#  TODO: 
#       randomize who you're hunting through the list for and how long things wait for


url_root = "https://genshin-impact.fandom.com/wiki/"

name_arr = []
with open("underscored_genshin_names.txt", "r", encoding="UTF-8") as character_name_file:
    name_with_newline = character_name_file.readlines()
    for name in name_with_newline:
        #  get rid of the newline chars
        name_arr.append(name.strip())

master_url_list = []

for person in name_arr:
    main_url = url_root + person
    this_persons_link_list = []
    # add each of the sub-urls to the master list
    this_persons_link_list.append(main_url)
    this_persons_link_list.append(main_url + "/Lore")
    this_persons_link_list.append(main_url + "/Voice-Overs")
    this_persons_link_list.append(main_url + "/Companion")
    
    this_persons_link_list.append(main_url + "/Outfits")
    # after constructing the sub-array, append the whole thing to the master list
    master_url_list.append(this_persons_link_list)
    
# ^^ output_format for a sample sub-arr within the master_url_list: [char, char/Lore, char/VA, char/Companion,  char/outfits,]


# If there are multiple outfits, get their names so the spider can crawl to other links from there
def outfit_set_scraper(url):
    headers = {"Connection":"keep-alive",'User-Agent': 'Mozilla/5.0'}
    html_page = requests.get(url, headers=headers)
    soup = bs(html_page.text, "html.parser")
    # Outfits are in a table format, as annotated here
    outfit_table = soup.find('table', class_='article-table')
    outfit_names = []
    if not outfit_table:
        print("Table not found")
        return
    # Find the <tbody> within the table
    tbody = outfit_table.find('tbody')
    if not tbody:
        print("Tbody not found")
        return
    # Then get all <tr> tags within the <tbody>
    rows = tbody.find_all('tr')
    for row in rows:
        # Find all <td> tags within the <tr>
        cells = row.find_all('td')
        # Check if there are at least 2 <td> tags, since we want to target the second one to get the name
        if len(cells) >= 2:
            # Print the text content of the second <td> tag
            outfit_name = cells[1].get_text(strip=True)
            if " " in outfit_name:
                # find and replace space with underscore in name
                outfit_name = outfit_name.replace(" ", "_")
            print(outfit_name)
            outfit_names.append(outfit_name)
        # if there's no content or the cells don't make sense, it's not our target, so ignore it
    return outfit_names


# ### PRESERVED: test a single outfit link to make sure the pattern hits correctly
dummy_link = "https://genshin-impact.fandom.com/wiki/Ganyu/Outfits"
# outfit_set_scraper(dummy_link)
# input("pausing execution...")

    # [!] confirm, can get outfit list from the outfits tab
 # out_list1 = outfit_scraper(dummy_link)
# print(out_list1)
# input("continue? 003")


# test for getting info from a single outfit, twilight blossom
twilight_url_string = "https://genshin-impact.fandom.com/wiki/Twilight_Blossom"

def genshin_article_info_scraper(url):
    headers = {"Connection":"keep-alive",'User-Agent': 'Mozilla/5.0'}
    html_page = requests.get(url, headers=headers)
    soup = bs(html_page.text, "html.parser")
    target_div = soup.find('div', id='mw-content-text')
    if target_div:
        juicy_text = target_div.get_text()
        print(juicy_text)
        return juicy_text
    else:
        input(f"problem occurred... check link{url}")

#  [!] confirmed ad-hoc outfit scraper can get the correct text info from the main list
# outfit_info_scraper_scraper(twilight_url_string)
# input("pausing 4")

# main 
# lore 
# voice over 
# [X] outfit 
# companion 

def main_page_description_scraper(url):
    headers = {"Connection":"keep-alive",'User-Agent': 'Mozilla/5.0'}
    html_page = requests.get(url, headers=headers)
    soup = bs(html_page.text, "html.parser")
    target_div = soup.find('div', id='mw-content-text')
    if target_div:
        all_p_tags = target_div.find_all('p')
# PRESERVED: hunt through adjacent tags to see how info is formatted, leave the target with the correct call after testing
        # print(all_p_tags[0])
        # print("-------")
        # print(all_p_tags[1])
        # NOTE: character names in Chinese will have the Hanzi for thei name listed in this [1] index above; irrelevant to current project though
        # print("-------")
        return all_p_tags[2].get_text()
    else:
        input("error cannot find target div : 005 ")

# PRESERVED: static testing, single requests, broken by user input
# main_page_description_scraper("https://genshin-impact.fandom.com/wiki/Kaveh")
# input("continue - 006")

# ===
#    Testing so far: main page, outfit set, and outfit info can all be navigated to and the info extracted via print statements 
# ===
test_name = "Cyno"
test_char_url = url_root + test_name
input(test_char_url)
main_page_info = main_page_description_scraper(test_char_url)
print(main_page_info)
# create a file for the main page description and inject the string data into it
with open("./english_character_info/" + test_name + "_main_description.txt", "w", encoding="UTF-8") as main_description_file:
    main_description_file.write(main_page_info)

input("pausing after finding main description - 007")
character_outfit_list = outfit_set_scraper(test_char_url + "/Outfits")
input("pausing after finding outfits listed above ... ")
# returns array of outfits found
if len(character_outfit_list) > 0:
    for outfit_name in character_outfit_list:
        outfit_info = genshin_article_info_scraper(url_root + outfit_name)
        print(f"above is information for the outfit: {outfit_name}")
        # There may be many outfits, so each set of clothes needs its own textfile, all labeled with the character info
            #  this will help matching the words to the outfit, when a hit is found in future searching
        with open("./english_character_info/" + test_name + "_" + outfit_name + "_outfit_description.txt", "w", encoding="UTF-8") as outfit_description_file:
            outfit_description_file.write(outfit_info)
        input("bp - 008")
else:
    print(f"No outfits found for {test_char_url}/Outfits")
    input("bp - 208")



lore_text = genshin_article_info_scraper(test_char_url + "/Lore")
# print(lore_text)
with open("./english_character_info/" + test_name + "_lore_collection.txt", "w", encoding="UTF-8") as lore_file:
    lore_file.write(lore_text)
input(f"lore written for {test_name} pausing - 009")

# get the voice over data, lots of good figure-of-speech samples!
voice_over_text = genshin_article_info_scraper(test_char_url + "/Voice-Overs")
# print(voice_over_text)
with open("./english_character_info/" + test_name + "_voice_overs.txt", "w", encoding="UTF-8") as voice_over_file:
    voice_over_file.write(voice_over_text)
input(f"lore written for {test_name} pausing - 009")
input(f"voice-over data written for {test_name} pausing - 010")

# get the companion article data (contains dialogue usually!)
companion_text = genshin_article_info_scraper(test_char_url + "/Companion")
# print(companion_text)
with open("./english_character_info/" + test_name + "_companion_dialogue.txt", "w", encoding="UTF-8") as companion_dialogue_file:
    companion_dialogue_file.write(companion_text)
input(f"companion dialogue data written for {test_name} pausing - 011")


print("Program complete! Check files being written")
#  For overview:https://genshin-impact.fandom.com/wiki/Ganyu/Voice-Overs
# https://genshin-impact.fandom.com/wiki/Kaveh
# https://genshin-impact.fandom.com/wiki/Ganyu

# For companion
# mw-content-text

# within outfits...
# https://genshin-impact.fandom.com/wiki/Ganyu/Outfits
#  scan for finding all outfit names



# test_urls = []
# clean_names_for_text_files = []
# for name in name_arr[52:63]:
#     test_urls.append(url_root + name)
#     # remove the %22 marking quotes in the name if it's found; cleans up file names
#     if "%22" in name:
#        name = name.replace("%22", "")
#     # otherwise, no change needs to be made and can be added straight
#     clean_names_for_text_files.append(name)
