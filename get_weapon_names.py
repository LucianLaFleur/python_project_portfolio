from bs4 import BeautifulSoup as bs
import requests

# ----------------------------------------------------------------------------------------

# static link values
url1 = "https://genshin-impact.fandom.com/wiki/Category:Weapons"
url2 = "https://genshin-impact.fandom.com/wiki/Category:Weapons?from=Uraku+Misugiri"

out_file_name = "wep_collection.txt"

# will hold all food names once grabbed
name_arr = []

def fetch_weapon_names(url, collection_list):
    headers = {"Connection":"keep-alive",'User-Agent': 'Mozilla/5.0'}
    html_page = requests.get(url, headers=headers)
    soup = bs(html_page.text, "html.parser")
    # food items are in categories that wrap up groups
        # lists are within each category
    page_content = soup.find('div', id='mw-content-text')

    target_li_list = page_content.find_all("li")
    for content in target_li_list:
        name = content.get_text(strip=True)
        if " " in name:
            name = name.replace(" ", "_")
        collection_list.append(name)
        
#  ---------- Process execution --------------------------------------------

# just manually call it twice because there's only 2 pages to browse through
fetch_weapon_names(url1, name_arr)
fetch_weapon_names(url2, name_arr)
print(len(name_arr))
input("shuffle and check length reduction from unique values...")
dupes_removed_food_name_arr = list(set(name_arr))
input(f"{len(dupes_removed_food_name_arr)} items in allegedly duplicate-removed list...\n enter to write items to text file")
with open(out_file_name, "w", encoding="UTF-8") as outfile:
    for item in dupes_removed_food_name_arr:
        outfile.write(item + "\n")

print(f"created [{out_file_name}]")


