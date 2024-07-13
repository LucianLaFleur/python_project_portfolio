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