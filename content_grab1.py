from bs4 import BeautifulSoup as bs
import requests
import time
import random
import genshin_scrape_common_functions

# ERROR DETECTED: in the output flags where there are problem pages

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

# ----------------------------------------------------------------------------------------

# static link values
url_root = "https://genshin-impact.fandom.com/wiki/"

#  confirmed! 
target_txt_file = "wep_collection.txt"

out_file_name = "weapon_descriptions.txt"

def fetch_content(item_name):
    print(f"-" * 34)
    print(f"{item_name} ---->> ")
    url = url_root + item_name
    headers = {"Connection":"keep-alive",'User-Agent': 'Mozilla/5.0'}
    html_page = requests.get(url, headers=headers)
    soup = bs(html_page.text, "html.parser")
    try:
        article_content = soup.find('div', id='mw-content-text')
        raw_text= article_content.get_text()
        return raw_text
    except:
        print(f"No data dound for page: {item_name}...")
        return f"ERROR DETECTED: {item_name} lacks data..."
        
#  ---------- Process execution --------------------------------------------
url_suffix_arr=[]
with open(target_txt_file, "r", encoding="UTF-8") as in_name_file:
    name_list = in_name_file.readlines()
    for item in name_list:
        url_suffix_arr.append(item.strip())

random.shuffle(url_suffix_arr)
# initialize a counter, and a list to hold each of the description lines that the spider gets when crawling across pages
counter_var = 0
all_content_text = []
for name in url_suffix_arr:
    counter_var += 1
    description_text = fetch_content(name)
    all_content_text.append(name + " : ")
    all_content_text.append(description_text + "\n")
    sleepy_time = genshin_scrape_common_functions.get_float_for_sleep()
    print(f"-" * 34)
    print(f"item [{counter_var}] of [{len(url_suffix_arr)}] complete, randomizing sleep time: {sleepy_time}")
    time.sleep(sleepy_time)

with open(out_file_name, "w", encoding="UTF-8") as name_file:
    for x in all_content_text:
        name_file.write(x)

print(f"created [{out_file_name}]")


