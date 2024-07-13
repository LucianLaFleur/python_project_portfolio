from bs4 import BeautifulSoup as bs
import requests
import time
import re
import genshin_scrape_common_functions

#  exceptional pages, not part of a pattern, but a list or category, but on their own...
#  remove url targeting structure based off names and make a manual list
#   add country-related urls via string manipulation 

# ----------------------------------------------------------------------------------------

# static link values
url_root = "https://genshin-impact.fandom.com/wiki/"
nation_names = ["Sumeru", "Mondstadt", "Liyue", "Inazuma", "Fontaine", "Natlan", "Snezhnaya"]

story_header_links = []
with open("event_quest_headers.txt", "r", encoding="UTF-8") as quest_header_name_file:
    quest_header_list = quest_header_name_file.readlines()
    for x in quest_header_list:
        if " " in x:
            x = x.replace(" ", "_")
        story_url = url_root + x.strip() + "/Story"
        story_header_links.append(story_url)

# nation_url_design_suffix = "/Design"
# nation_url_history_suffix = "/History"
# nation_url_culture_suffix = "/Culture"

# manual urls to add...
url1 = "https://genshin-impact.fandom.com/wiki/Imaginarium_Theater/Fortune_Slips"
url2 = "https://genshin-impact.fandom.com/wiki/Imaginarium_Theater/Voice-Overs"
url3 = "https://genshin-impact.fandom.com/wiki/Iridescent_Arataki_Rockin%27_for_Life_Tour_de_Force_of_Awesomeness/Story"
url4 = "https://genshin-impact.fandom.com/wiki/This_Ain%27t_Your_Daddy%27s_Iridescence_Tour..."
url5 = "https://genshin-impact.fandom.com/wiki/...It%27s_the_Iridescent_Arataki_Rockin%27_for_Life_Tour_de_Force_of_Awesomeness!"
url_arr = [url1, url2, url3, url4, url5]
for nation in nation_names:
    hist_url = url_root + nation + "/Design"
    design_url = url_root + nation + "/History"
    culture_url = url_root + nation + "/Culture"
    url_arr.append(hist_url)
    url_arr.append(design_url)
    url_arr.append(culture_url)
    print(f"{nation} urls added to target arr")

with open("filtered_books.txt", "r", encoding="UTF-8") as book_file:
    all_book_lines = book_file.readlines()
    for line in all_book_lines:
        bare_line = line.strip()
        url_arr.append(url_root + bare_line)

print(f"*" * 35)
print(url_arr)
# for i in url_arr:
#     print(i)

input("pausing 234234")

out_file_name = "misc_collection_output.txt"

# init an arr to get bad urls
problematic_url_list = []

def fetch_content(url):
    print(f"-" * 34)
    print(f"{url} ---->> ")
    headers = {"Connection":"keep-alive",'User-Agent': 'Mozilla/5.0'}
    html_page = requests.get(url, headers=headers)
    soup = bs(html_page.text, "html.parser")
    try:
#       content for all should be in id='mw-content-text'
        article_content = soup.find('div', id='mw-content-text')
        raw_text= article_content.get_text()
        return raw_text
    except:
        print(f"No data dound for page: {url}...")
        problematic_url_list.append(url)
        return f"ERROR DETECTED: {url} lacks data..."
        
#  ---------- Process execution --------------------------------------------

# initialize a counter, and a list to hold each of the description lines that the spider gets when crawling across pages
counter_var = 0
all_content_text = []
for name in url_arr:
    counter_var += 1
    description_text = fetch_content(name)
    all_content_text.append(description_text + "\n")
    sleepy_time = genshin_scrape_common_functions.get_float_for_sleep()
    print(f"-" * 34)
    print(f"item [{counter_var}] of [{len(url_arr)}] complete, randomizing sleep time: {sleepy_time}")
    time.sleep(0.6)

with open(out_file_name, "w", encoding="UTF-8") as name_file, open("misc_bad_urls", 'w', encoding="UTF-8") as bad_misc_file:
    for x in all_content_text:
        name_file.write(x)
    for bad_item in problematic_url_list:
        bad_misc_file.write(bad_item)

print(f"created [{out_file_name}]")


