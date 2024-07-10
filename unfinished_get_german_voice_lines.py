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

    p_tag_list = target_div_list[0].find_all('p')
# due to inconsistent site structure, the voice-lines may be in a table as opposed to in text. Lisa has <p> tags regularly while 

    # first_p_tag = 
    for tag in p_tag_list:
        actual_words = tag.get_text()
        dialogue_list.append(actual_words)
    return dialogue_list

test_url = "https://genshin-impact.fandom.com/de/wiki/Amber/Stimme"

test_list_of_lines = run_scrape_for_voice_lines(test_url)

target_output_name = input(f"Enter a filename for testing the url\n {test_url}\n >> ")
file_suffix = ".txt"
with open(target_output_name + file_suffix, "w", encoding='utf-8') as my_file:
    for chunk in test_list_of_lines:
        my_file.write(chunk)


print(f"Execution complete: {target_output_name}{file_suffix} created")


# literature, philosophy, 
# german culture, fairy tales,
#  song lyrics, pop culture, news headlines
#  motivational quotes on the topic of X.

# collection of text data from traditional german fairy tales 