from bs4 import BeautifulSoup as bs
import requests
import time
textfile_full_of_names = "underscored_genshin_names.txt"

#  Example for finding the voice lines for the character, Lisa
# "https://genshin-impact.fandom.com/de/wiki/Lisa/Stimme"

# I hate looking at wikis that are overrun with ads so badly you can't focus on the screen
# a scraper and command line can fix that...

# base url path for a character; it will have the character's name at the end of the template string
url_template = "https://genshin-impact.fandom.com/de/wiki/"
#  =======================================

def run_scrape(url):
    dialogue_list = []
    headers = {"Connection":"keep-alive",'User-Agent': 'Mozilla/5.0'}
    html_page = requests.get(url, headers=headers)
    soup = bs(html_page.text, "html.parser")
    target_div_list = soup.find_all('div', class_='mw-parser-output')

    for target_div_tag in target_div_list:
        word_salad = target_div_tag.get_text()
        dialogue_list.append(word_salad)
    return dialogue_list

main_page_list = []
# read from the textfile with the list of names, use UTF-8 because special characters might be a thing
with open(textfile_full_of_names, "r", encoding="UTF-8") as name_file:
    name_list = name_file.readlines()
    for name in name_list:
        peeled_name = name.strip()
        # Sanity check to see if we're grabbing the text we want to.
        # print(url_template + peeled_name)
        main_page_list.append(url_template + peeled_name)

length_of_list = len(main_page_list)
name_list_index = 0
for character_url in main_page_list:
    if name_list_index > 200:
        print("halting program, error occured")
        input("please cancel this program with ctrl + c")
    char_name = name_list[name_list_index].strip()
    
    char_main_word_salad = run_scrape(character_url)
    with open(f"z_{char_name}_main_page.txt", "w", encoding="UTF-8") as output_file:
        output_file.writelines(char_main_word_salad)
    print(f"Info for obtained for [ {char_name} ] ... ")
    time.sleep(1.3)
    name_list_index += 1






# with open("all_genshin_main_links1.txt", "w", encoding="UTF-8") as output_file:
#     for item in dummy_list:
#         output_file.write(item + "\n")


# Sangonomiya_Kokomi
# test_name = "Amber"
# test_url = url_template + test_name
# print(f"Running test for {test_name}'s main page")

# test_list_of_lines = run_scrape(test_url)

# target_output_name = input(f"Enter a filename for testing the url\n {test_url}\n >> ")
# file_suffix = ".txt"
# with open(target_output_name + file_suffix, "w", encoding='utf-8') as my_file:
#     for chunk in test_list_of_lines:
#         my_file.write(chunk)


# print(f"Execution complete: {target_output_name}{file_suffix} created")

print(f"Execution complete: done")
