from bs4 import BeautifulSoup as bs
import requests
import time
import re

# structure:
# https://genshin-impact.fandom.com/wiki/name

url_root = "https://genshin-impact.fandom.com/wiki/"

name_arr = []
with open("underscored_genshin_names.txt", "r", encoding="UTF-8") as character_name_file:
    name_with_newline = character_name_file.readlines()
    for name in name_with_newline:
        #  get rid of the newline chars
        name_arr.append(name.strip())

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


dummy_link = "https://genshin-impact.fandom.com/wiki/Ganyu/Outfits"

# test for getting info from a single outfit, twilight blossom
twilight_url_string = "https://genshin-impact.fandom.com/wiki/Twilight_Blossom"

def genshin_article_info_scraper(url):
    headers = {"Connection":"keep-alive",'User-Agent': 'Mozilla/5.0'}
    html_page = requests.get(url, headers=headers)
    soup = bs(html_page.text, "html.parser")
    target_div = soup.find('div', id='mw-content-text')
    if target_div:
        juicy_text = target_div.get_text()
        # print(juicy_text)
        return juicy_text
    else:
        input(f"problem occurred... check link{url}")


def main_page_description_scraper(url):
    headers = {"Connection":"keep-alive",'User-Agent': 'Mozilla/5.0'}
    html_page = requests.get(url, headers=headers)
    soup = bs(html_page.text, "html.parser")
    target_div = soup.find('div', id='mw-content-text')
    if target_div:
        all_p_tags = target_div.find_all('p')
        return all_p_tags[2].get_text()
    else:
        input("error cannot find target div : 005 ")

# ===
#    Testing so far: main page, outfit set, and outfit info can all be navigated to and the info extracted via print statements 
# [X] main 
# [X] outfit 
# lore 
# voice over 
# companion 
#  === 
# Changes: not doing each category in own mini file, but all info for all characters in one output textfile
# removed iteration to add an array of character urls up front, within the process execution, the pattern for making the urls can be added to each name,
# also, this makes it clearer for diagnosing problems with any given article type...
# ===

def get_char_info_from_name(test_name):
    juicy_text_list = []
    test_char_url = url_root + test_name
    main_page_info = main_page_description_scraper(test_char_url)
    print(f"writing main page info for {test_name}...")
    time.sleep(9.8)
    juicy_text_list.append(main_page_info)

    character_outfit_list = outfit_set_scraper(test_char_url + "/Outfits")
    # returns array of outfits found
    if len(character_outfit_list) > 0:
        for outfit_name in character_outfit_list:
            outfit_info = genshin_article_info_scraper(url_root + outfit_name)
            print("cooling down...")
            time.sleep(5.7)
            print(f"info written for outfit: {outfit_name}")
            juicy_text_list.append(outfit_info)
    else:
        print(f"No outfits found for {test_char_url}/Outfits")
    lore_text = genshin_article_info_scraper(test_char_url + "/Lore")
    print(f"writing lore for {test_name}...")
    time.sleep(7.6)
    juicy_text_list.append(lore_text)
    voice_over_text = genshin_article_info_scraper(test_char_url + "/Voice-Overs")
    print(f"writing Voice Overs for {test_name}...")
    time.sleep(8.9)
    juicy_text_list.append(voice_over_text)
    companion_text = genshin_article_info_scraper(test_char_url + "/Companion")
    print(f"writing companion data for {test_name}...")
    time.sleep(6.6)
    juicy_text_list.append(companion_text)

    # declare the regex pattern for looking for text content
    pattern = re.compile(r'^(?!\d).{33,}$')
# About (r'^(?!\d)')
#     1)    ^ asserts the position at the start of the string.
#     2)    (?!\d) is a negative lookahead assertion that asserts that what immediately follows the current position is not a digit (\d).
#     3)    .{33,} matches any character (except newline) at least 33 times. Combined with the preceding character assertion, this ensures the string is at least 34 characters long.

    with open("./char_info_english/zz_garbage_" + test_name + ".txt", "w", encoding="UTF-8") as char_file:
        for text_chunk in juicy_text_list:
            char_file.write(text_chunk)

# PRESERVED...
# yeah, this is ineffecient, but it works, and trying to fix it messed things up, so whatever

    with open("./char_info_english/zz_garbage_" + test_name + ".txt", "r", encoding="UTF-8") as fresh_file, open("./char_info_english/" + "purified_" + test_name, 'w', encoding="UTF-8") as outfile:
        impure_arr = fresh_file.readlines()
        filtered_lines = [line for line in impure_arr if pattern.match(line)]
        # give a set of lines that only match the filter criteria mentioned above
        for x in filtered_lines:
            outfile.write(x)
        
    print(f"char data written for {test_name} in test scrape subfolder... now pausing - 009")

randomized_name_arr = list(set(name_arr))

for name in randomized_name_arr:
    get_char_info_from_name(name)
    print(f"pausing after getting info for {name}")
    time.sleep(5)

print("Program complete! Check files being written")
