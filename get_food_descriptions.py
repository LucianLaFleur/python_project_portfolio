from bs4 import BeautifulSoup as bs
import requests
import time
import random

url_root = "https://genshin-impact.fandom.com/wiki/"

def fetch_food_description(food_name):
    print(f"-" * 34)
    print(f"{food_name} ---->> ")
    url = url_root + food_name
    # input(f"url check: {url}")
    headers = {"Connection":"keep-alive",'User-Agent': 'Mozilla/5.0'}
    html_page = requests.get(url, headers=headers)
    soup = bs(html_page.text, "html.parser")
    #  the food description text is found in the following content item
    food_description_content = soup.find('div', class_='pi-data-value').get_text()
    print(food_description_content)
    return food_description_content

def get_float_for_sleep():
    # float will be between 5.1 and 8.9 seconds, reasonable enough throttling
    # ...
# first, build up the ranges
    seconds = range(5,9)
    tenths_of_seconds = range(1,10)
# Randomly select an item from the range
    unconverted_int = random.choice(tenths_of_seconds)
    # divide by 10 to put in the tenths place
    converted_tenth = float(unconverted_int/10)
    whole_seconds = float(random.choice(seconds))
    result_float = whole_seconds + converted_tenth
        #  e.g --> 3.4
    return result_float

name_arr = []
with open("food_name_collection.txt", "r", encoding="UTF-8") as food_name_file:
    food_name_list = food_name_file.readlines()
    for item in food_name_list:
        name_arr.append(item.strip())

counter_var = 0
all_descriptions = []
for name in name_arr[63:67]:
    counter_var += 1
    description_text = fetch_food_description(name)
    all_descriptions.append(name + " : ")
    all_descriptions.append(description_text + "\n")
    sleepy_time = get_float_for_sleep()
    print(f"-" * 34)
    print(f"item [{counter_var}] of [{len(name_arr)}] complete, randomizing sleep time: {sleepy_time}")
    time.sleep(sleepy_time)


with open("./food_descriptions/" + "all_food_descriptions.txt", "w", encoding="UTF-8") as food_name_file:
    for x in all_descriptions:
        food_name_file.write(x)

print("writing complete!")
# def get_and_write_food_descriptions(food_name):