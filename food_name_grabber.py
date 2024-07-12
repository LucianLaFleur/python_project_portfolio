from bs4 import BeautifulSoup as bs
import requests
# The food descriptions are the only target among the items. 

# 2 pages, static values listing all food items
food_list1 = "https://genshin-impact.fandom.com/wiki/Category:Food"
food_list2 = "https://genshin-impact.fandom.com/wiki/Category:Food?from=Mondstadt+Grilled+Fish"
food_pages = [food_list1, food_list2]
# will hold all food names once grabbed
food_name_arr = []

def fetch_food_names_and_add_to_collection_list(url, collection_list):
    headers = {"Connection":"keep-alive",'User-Agent': 'Mozilla/5.0'}
    html_page = requests.get(url, headers=headers)
    soup = bs(html_page.text, "html.parser")
    # food items are in categories that wrap up groups
        # lists are within each category
    page_content = soup.find('div', id='mw-content-text')

    target_li_list = page_content.find_all("li")
    for content in target_li_list:
        food_name1 = content.get_text(strip=True)
        if " " in food_name1:
            food_name1 = food_name1.replace(" ", "_")
        collection_list.append(food_name1)
        
    # dummy_arr = []
    # for food_item in all_list_items:
    #     dummy_arr.append(food_item.get_text())
    # return dummy_arr
#  ABOVE, PRESERVED: instead of making and returning a dummy arr, I am running this function many times
        # Thus, I pass in an arr, adding items through the function, needing no return value.
            # Below solution needs fewer lines of code too, so it's neat

#  ---------- Process execution --------------------------------------------

# just manually call it twice because there's only 2 pages to browse through
fetch_food_names_and_add_to_collection_list(food_list1, food_name_arr)
fetch_food_names_and_add_to_collection_list(food_list2, food_name_arr)
print(len(food_name_arr))
input("shuffle and check length reduction from unique values...")
dupes_removed_food_name_arr = list(set(food_name_arr))
input(f"{len(dupes_removed_food_name_arr)} items in allegedly duplicate-removed list...\n enter to write items to text file")
with open("food_name_collection.txt", "w", encoding="UTF-8") as outfile:
    for item in dupes_removed_food_name_arr:
        outfile.write(item + "\n")

print("created [food_name_collection.txt]")


