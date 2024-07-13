from bs4 import BeautifulSoup as bs
import requests
import time
import random
import genshin_scrape_common_functions

# Sample hangout, with dialogue...
# https://genshin-impact.fandom.com/wiki/Gang_Bylaws

# Sample quest, with dialogue...
# https://genshin-impact.fandom.com/wiki/Unknown_Star

# TEST below to see if program can grab text data from each
# https://genshin-impact.fandom.com/wiki/Iridescent_Arataki_Rockin%27_for_Life_Tour_de_Force_of_Awesomeness/Story
# https://genshin-impact.fandom.com/wiki/This_Ain%27t_Your_Daddy%27s_Iridescence_Tour...
# https://genshin-impact.fandom.com/wiki/...It%27s_the_Iridescent_Arataki_Rockin%27_for_Life_Tour_de_Force_of_Awesomeness!

# event chapter list; all of these need /story attached to draw out important data:
# .... draw in from a text file...

# imaginarium voice overs:
# https://genshin-impact.fandom.com/wiki/Imaginarium_Theater/Voice-Overs
# fortune slip info
# https://genshin-impact.fandom.com/wiki/Imaginarium_Theater/Fortune_Slips

#  nation_names = [Sumeru, Mondstadt, Liyue,
# Inazuma, Fontaine, Natlan, Snezhnaya]

# nation_url_design_suffix = "/Design"
# nation_url_history_suffix = "/History"
# nation_url_culture_suffix = "/Culture"
#       should be in id='mw-content-text'

# furnishing items need extraction similar to food items

# ----------------------------------------------------------------------------------------

# static link values
url_root = "https://genshin-impact.fandom.com/wiki/"


target_txt_file = "furnishing_name_collection.txt"
out_file_name = "furnishing_data_big_text_output.txt"

def fetch_description(item_name):
    print(f"-" * 34)
    print(f"{item_name} ---->> ")
    url = url_root + item_name
    # input(f"url check: {url}")
    headers = {"Connection":"keep-alive",'User-Agent': 'Mozilla/5.0'}
    html_page = requests.get(url, headers=headers)
    soup = bs(html_page.text, "html.parser")
    #  the food description text is found in the following content item
    try:
        description_content = soup.find_all('div', class_='pi-data-value')
#  PRESERVED:
    # insonsistent structure, need to find which item within the array of items contains the description
        # mini_counter = 0
        # for x in description_content:
        #     mini_counter += 1
        #     print(f"item {mini_counter} ---------------- ")
        #     given_text = x.get_text()
        #     print(given_text)
        # input("pause 202")
# ALSO PRESERVED
    #  need to investigate which index's text correctly appears with the content.
        # print(description_content)
        # input("pause 017")
        mini_arr = []
        for x in description_content:
            desc1 = x.get_text()
            print(desc1)
            mini_arr.append(x)
        return mini_arr
    except:
        print(f"No description found for {item_name}...")
        return f"{item_name} lacks data..."
        
#  ---------- Process execution --------------------------------------------
name_arr=[]
with open(target_txt_file, "r", encoding="UTF-8") as in_name_file:
    food_name_list = in_name_file.readlines()
    for item in food_name_list:
        name_arr.append(item.strip())

random.shuffle(name_arr)
# initialize a counter, and a list to hold each of the description lines that the spider gets when crawling across pages
counter_var = 0
all_descriptions = []
for name in name_arr:
    counter_var += 1
    description_text_arr = fetch_description(name)
    all_descriptions.append(name + " : ")
    for text_item in description_text_arr:
        all_descriptions.append(text_item.get_text() + "\n")
    sleepy_time = genshin_scrape_common_functions.get_float_for_sleep()
    print(f"-" * 34)
    print(f"item [{counter_var}] of [{len(name_arr)}] complete, randomizing sleep time: {sleepy_time}")
    time.sleep(sleepy_time)

with open(out_file_name, "w", encoding="UTF-8") as name_file:
    for x in all_descriptions:
        name_file.write(x)

print(f"created [{out_file_name}]")


