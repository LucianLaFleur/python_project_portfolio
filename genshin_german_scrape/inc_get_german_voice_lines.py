from bs4 import BeautifulSoup as bs
import requests
import re
#  Example for finding the voice lines for the character, Lisa
# "https://genshin-impact.fandom.com/de/wiki/Lisa/Stimme"

# I hate looking at wikis that are overrun with ads so badly you can't focus on the screen
# a scraper and command line can fix that...

# base url path for a character; it will have the character's name at the end of the template string
url_template = "https://genshin-impact.fandom.com/de/wiki/"
# after the name, append "/Stimme" to find the voice lines, if any.
                        # (Voice)
voice_suffix_for_url = "/Stimme"
# Some characters also have "background information". This might be a good source of sentences too
background_suffix_for_url = "/Figurenhintergrund"
#  most articles on clothing are empty, but some might have data...
clothing_suffix_for_url = "/Kleidung"

clean_name_list = []
with open("all_names.txt", "r") as my_file:
    bad_name_list = my_file.readlines()
    #  input will initially have /n at the end of each name, so let's remove that with .strip()
    for name in bad_name_list:
        newline_removed_name = name.strip()
        clean_name_list.append(newline_removed_name)

#  =======================================

def run_scrape_for_voice_lines(url):
    dialogue_list = []
    headers = {"Connection":"keep-alive",'User-Agent': 'Mozilla/5.0'}
    html_page = requests.get(url, headers=headers)
    soup = bs(html_page.text, "html.parser")
    
    content1 = soup.find('div', id="mw-content-text")
    return content1.get_text()
    
# SAVED FOR DEVELOPMENT LOGGING : Test to see if multiple divs are returned by the class-name targeting, since it's not a unique ID
    # Was tested with a single, static URL --> run_scrape_for_voice_lines("https://genshin-impact.fandom.com/de/wiki/Lisa/Stimme")
    # target_div_list = soup.find('div', class_='mw-parser-output')
    # print(len(target_div_list))
    # Above output gave 1 hit, showing we have a single <div> in the bag
    #   Thus, needed to change "find all" to "find" so we're just dealing with that one item and not an array of a single item.

test_list_of_lines = run_scrape_for_voice_lines("https://genshin-impact.fandom.com/de/wiki/Lisa/Stimme")

#  init a list to hold the text filtered after writing html to txt as shorthand to get lines via newline.
split_up_lines = test_list_of_lines.split("\n")
target_output_name = "dummytest004"
file_suffix = ".txt"

filter_words = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "[]"]

text_only_lines = []
pattern = re.compile(r'[A-Za-z]')
for line in split_up_lines:
        if pattern.search(line):
            if not any(filter_word in line for filter_word in filter_words):
                text_only_lines.append(line)

for x in text_only_lines:
    print(x)

# with open(target_output_name + file_suffix, "w", encoding='utf-8') as my_file:
#     for chunk in test_list_of_lines:
#         my_file.write(chunk)

# with open(target_output_name + file_suffix, "r", encoding='utf-8') as fresh_file:
#     # filter out anything that doesn't contain at least some letter in it
#     pattern = re.compile(r'[A-Za-z]')
#     for line in fresh_file.readlines():
#         print(line)
#         input("pause444")
#         if pattern.search(line):
#             text_only_lines.append(line)


input("pause0t34j-t43")





print(f"Execution complete: {target_output_name}{file_suffix} created")

#  ================
#   dd_tags = phrases_dl.find_all('dd') -> get all instances of a tag
        #       print(dd.get_text()) --> git the html text content within a tag
        # soup.find_all('div', class_='potato') -> find all of a certain class
#  ================
#  when there is no collection, keyword is...
# momentan noch keinen Text
#  Also, 
#  a div with className = "noarticletext" indicated the article is not available
#  Confirmed, the classname "noarticletext" will not appear on a content-bearing page

