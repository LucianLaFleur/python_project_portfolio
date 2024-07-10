from bs4 import BeautifulSoup as bs
import requests


# structure:
# https://genshin-impact.fandom.com/wiki/Annette
# https://genshin-impact.fandom.com/wiki/NPC/List

url = "https://genshin-impact.fandom.com/wiki/NPC/List"

file_name = "genshin_npc_name_list.txt"

# https://genshin-impact.fandom.com/wiki/I._Ivanovna_N.
# https://genshin-impact.fandom.com/wiki/Dr._Livingstone
# https://genshin-impact.fandom.com/wiki/%22Kichiboushi%22

# id = mw-content-text
#  then get all text from within

def scrape_npc_names():
    # names_list = []
    # init the names list that we ultimately want for the output
    headers = {"Connection":"keep-alive",'User-Agent': 'Mozilla/5.0'}
    html_page = requests.get(url, headers=headers)
    soup = bs(html_page.text, "html.parser")
    npc_name_div = soup.find('div', class_='mw-parser-output')
    
# Preserved: Make sure there's only 1 item found for our target    
    # num_items_returned = len(npc_name_div)
    # print(f"{num_items_returned} items found")

    all_li_content = npc_name_div.find_all('li')
    return all_li_content


#  Process execution -----------------------------------------------------------------

# get all the li content from the main target div
li_tag_collection = scrape_npc_names()

list_of_actual_text = []
for li_tag in li_tag_collection:
    actual_words = li_tag.get_text()
    list_of_actual_text.append(actual_words)

# These names also have to be space-purified to work
space_items = 0
with open(file_name, "w", encoding="UTF-8") as outfile:
    for item in list_of_actual_text:
        if " " in item:
            print(f"Space detected in {item}")
            underscored_item = item.replace(" ", "_")
            print(f"Changed to --> {underscored_item}")
            outfile.write(underscored_item + "\n")
            space_items += 1
        else:
            outfile.write(item + "\n")

print(f"{file_name} created!")
print(f"{space_items} items with spaces corrected")
