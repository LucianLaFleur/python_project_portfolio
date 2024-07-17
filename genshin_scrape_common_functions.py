from bs4 import BeautifulSoup as bs
import requests
import random
import re

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

def remove_lines_lacking_letters(input_textfile_name, output_textfile_name):
    # Define the pattern to match lines that contain text characters (not just digits or special characters)
    pattern = re.compile(r'[A-Za-z]')

    # Open the input and output files
    with open(input_textfile_name, 'r', encoding="UTF-8") as infile, open(output_textfile_name, 'w', encoding="UTF-8") as outfile:
        for line in infile:
            # Check if the line contains text characters
            if pattern.search(line):
                # Write the line to the output file
                outfile.write(line)
            # else, ignore the line because it's either blank or just a number

def general_genshin_info_scraper(url):
    headers = {"Connection":"keep-alive",'User-Agent': 'Mozilla/5.0'}
    html_page = requests.get(url, headers=headers)
    soup = bs(html_page.text, "html.parser")
    target_div = soup.find('div', id='mw-content-text')
    if target_div:
        juicy_text = target_div.get_text()
        print(juicy_text)
        return juicy_text
    else:
        input(f"problem occurred... check link{url}")

# example, used for removing spaces and number-only lines from the misc-content scrape:
# remove_lines_lacking_letters("misc_collection_output.txt", "purified_misc_content.txt")

#  --------------------------------------------------------------------------------------------------
# .pop() removes last, sanity check....
# potato = [1, 2, 3, 4, 5]
# p1 = potato.pop()
# print(p1)
# print(potato)
# input("pause....")

#  --------------------------------------------------------------------------------------------------
# Find n-th item in a set while scraping

# def find_nth_item_in_scrape(url):
#   headers = {"Connection":"keep-alive",'User-Agent': 'Mozilla/5.0'}
#   html_page = requests.get(url, headers=headers)
#   soup = bs(html_page.text, "html.parser")
#   # Find the <div> tag with the id "mw-content-text"
#   content_div = soup.find('div', id='mw-content-text')
#   # Find the first child <div> tag within the content_div
#   first_child_div = content_div.find('div')
#   # Find all <dl> tags within the first_child_div
#   dl_tags = first_child_div.find_all('dl')

#  # EXAMPLE, hunting for the 6th <dl> on the page, thus appearing at idx 5 
#   target_dl = dl_tags[5]

#   # Find all <dd> tags within the target <dl> tag
#   dd_tags = target_dl.find_all('dd')

#   # Print the text content of each <dd> tag
#   for dd in dd_tags:
#       print(dd.get_text())
  
# print("Reminder crtl+w closes current tab")

#  --------------------------------------------------------------------------------------------------
# For keyword search instead .... 
# # Define the list of keywords to search for
# keywords = ['keyword1', 'keyword2', 'keyword3']  # Replace with your actual keywords

# # Iterate over all <p> tags within the content_div
# for p_tag in content_div.find_all('p'):
#     p_text = p_tag.get_text()
#     # Check if any of the keywords are in the text content of the <p> tag
#     if any(keyword in p_text for keyword in keywords):
#         # Print the entire text content of the <p> tag
#         print(p_text)
