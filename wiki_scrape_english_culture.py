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
    this_persons_link_list.append(main_url + "/Outfits")
    this_persons_link_list.append(main_url + "/Companion")
    # after constructing the sub-array, append the whole thing to the master list
    master_url_list.append(this_persons_link_list)
    
# print(master_url_list[52:55])
# input("pause 002 ")

#  For overview:https://genshin-impact.fandom.com/wiki/Ganyu/Voice-Overs

# mw-content-text
# 4th child p tag 

# For companion
# mw-content-text

# within outfits...
# https://genshin-impact.fandom.com/wiki/Ganyu/Outfits
#  scan for finding all outfit names


# If there are multiple outfits, get their names so the spider can crawl to other links from there
def outfit_scraper(url):
    headers = {"Connection":"keep-alive",'User-Agent': 'Mozilla/5.0'}
    html_page = requests.get(url, headers=headers)
    soup = bs(html_page.text, "html.parser")
    
    # Find the table with class 'article-table'
    outfit_table = soup.find('table', class_='article-table')
    
    # start up a list to collect the outfit names
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
        # Check if there are at least 2 <td> tags, since we want to target the second one
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
# outfit_scraper(dummy_link)
# input("pausing execution...")

    # [!] confirm, can get outfit list from the outfits tab
 # out_list1 = outfit_scraper(dummy_link)
# print(out_list1)
# input("continue? 003")


# ad-hoc list 
twilight_url_string = "https://genshin-impact.fandom.com/wiki/Twilight_Blossom"

def ad_hoc_scraper(url):
    headers = {"Connection":"keep-alive",'User-Agent': 'Mozilla/5.0'}
    html_page = requests.get(url, headers=headers)
    soup = bs(html_page.text, "html.parser")
    target_div = soup.find('div', id='mw-content-text')
    if target_div:
        print(target_div.get_text(strip=True))

#  [!] confirm ad-hoc scraper can get the correct text info from the main list
# ad_hoc_scraper(twilight_url_string)
# input("pausing 4")

test_urls = []
clean_names_for_text_files = []
for name in name_arr[52:63]:
    test_urls.append(url_root + name)
    # remove the %22 marking quotes in the name if it's found; cleans up file names
    if "%22" in name:
       name = name.replace("%22", "")
    # otherwise, no change needs to be made and can be added straight
    clean_names_for_text_files.append(name)
