from bs4 import BeautifulSoup as bs
import requests

# ----------------------------------------------------------------------------------------

# static link values
url1 = "https://genshin-impact.fandom.com/wiki/Furnishing/List"

out_file_name = "furnishing_name_collection.txt"

# will hold all food names once grabbed
name_arr = []

def get_names(url, collection_list):
    headers = {"Connection":"keep-alive",'User-Agent': 'Mozilla/5.0'}
    html_page = requests.get(url, headers=headers)
    soup = bs(html_page.text, "html.parser")
    # food items are in categories that wrap up groups
        # lists are within each category
    page_content = soup.find('div', class_='columntemplate')

    target_li_list = page_content.find_all("li")
    for content in target_li_list:
        name = content.get_text(strip=True)
        if " " in name:
            name = name.replace(" ", "_")
        collection_list.append(name)
        
#  ---------- Process execution --------------------------------------------

# just manually call it twice because there's only 2 pages to browse through
get_names(url1, name_arr)
print(f"Starting items: {len(name_arr)}")
dupes_removed_food_name_arr = list(set(name_arr))
input(f"{len(dupes_removed_food_name_arr)} items in allegedly duplicate-removed list...\n enter to write items to text file")
with open(out_file_name, "w", encoding="UTF-8") as outfile:
    for item in dupes_removed_food_name_arr:
        outfile.write(item + "\n")

print(f"created [{out_file_name}]")


