from bs4 import BeautifulSoup as bs
import requests
import time
import random
import genshin_scrape_common_functions

# static link values
url_root = "https://genshin-impact.fandom.com/wiki/"

#  confirmed! 
target_txt_file = "hangouts_names.txt"

out_file_name = "hangout_content_text.txt"

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
    time.sleep(0.5)

with open(out_file_name, "w", encoding="UTF-8") as name_file:
    for x in all_content_text:
        name_file.write(x)

print(f"created [{out_file_name}]")


