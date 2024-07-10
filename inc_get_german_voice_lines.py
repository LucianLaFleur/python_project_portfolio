from bs4 import BeautifulSoup as bs
import requests
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
clean_name_list = []

# with open("all_genshin_names.txt", "r") as my_file:
#     genshin_name_list = my_file.readlines()
#     #  input will initially have /n at the end of each name, so let's remove that with .strip()
#     for name in genshin_name_list:
#         newline_removed_name = name.strip()
# #  Conditional handles names with spaces
#     # url names cannot process spaces, so find them and replace with an underscore instead
#         if " " in newline_removed_name:
#             # re-declare the variable to include the underscore if there's a space found; we want to overwrite before appending to the list
#             newline_removed_name = newline_removed_name.replace(" ", "_")
#         clean_name_list.append(newline_removed_name)


# character_url_collection = []
# for person in clean_name_list:
#     chatacter_data_url_list = []
#     # basic string concatenation should work (NYI)
#     base_url = url_template + person
#     voice_line_url = base_url + voice_suffix_for_url
#     # add the base url to the character url list
#     character_url_collection.append(base_url)
#     # add voice line to character url list
#     character_url_collection.append(voice_line_url)  
#     # [ ! ] append the whole character url list to the collection
#         #  Expected: collection = [[wiki/bob, wiki/bob/Stimme ...], [wiki/sally, wiki/sally/Stimme...]]
#     character_url_collection.append(character_url_collection)  





#  =======================================

def run_scrape_for_voice_lines(url):
    dialogue_list = []
    headers = {"Connection":"keep-alive",'User-Agent': 'Mozilla/5.0'}
    html_page = requests.get(url, headers=headers)
    soup = bs(html_page.text, "html.parser")
    target_div_list = soup.find('div', class_='mw-parser-output')
    
# SAVED FOR DEVELOPMENT LOGGING : Test to see if multiple divs are returned by the class-name targeting, since it's not a unique ID
    # Was tested with a single, static URL --> run_scrape_for_voice_lines("https://genshin-impact.fandom.com/de/wiki/Lisa/Stimme")

    # target_div_list = soup.find('div', class_='mw-parser-output')
    # print(len(target_div_list))

    # Above output gave 1 hit, showing we have a single <div> in the bag
    #   Thus, needed to change "find all" to "find" so we're just dealing with that one item and not an array of a single item.

    p_tag_list = target_div_list.find_all('p')
    for tag in p_tag_list:
        actual_words = tag.get_text()
        dialogue_list.append(actual_words)
    return dialogue_list


test_list_of_lines = run_scrape_for_voice_lines("https://genshin-impact.fandom.com/de/wiki/Lisa/Stimme")

target_output_name = "lisa_test_2"
file_suffix = ".txt"
with open(target_output_name + file_suffix, "w", encoding='utf-8') as my_file:
    for chunk in test_list_of_lines:
        my_file.write(chunk)


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


# https://genshin-impact.fandom.com/de/wiki/Arataki_Itto
#  Profiles may have interesting description examples within appearance and personality pieces