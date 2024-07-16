from bs4 import BeautifulSoup as bs
import requests
import re


# ----------------------------------------------------------------------------------------

# static link values
url1 = "https://genshin-impact.fandom.com/wiki/Book"

out_file_name = "book_names.txt"

def fetch_book_names(url):
    headers = {"Connection":"keep-alive",'User-Agent': 'Mozilla/5.0'}
    html_page = requests.get(url, headers=headers)
    soup = bs(html_page.text, "html.parser")
    # food items are in categories that wrap up groups
        # lists are within each category
    page_content = soup.find('div', id='mw-content-text')
    content_text = page_content.get_text()
    return content_text
        
#  ---------- Process execution --------------------------------------------

# just manually call it twice because there's only 2 pages to browse through
book_names = fetch_book_names(url1)
input("shuffle and check length reduction from unique values...")
with open(out_file_name, "w", encoding="UTF-8") as outfile:
    outfile.write(book_names)

print(f"created [{out_file_name}]\n filtering out any garbage space-lines...")

# Define the pattern to match lines that contain text characters (not just digits or special characters)
pattern = re.compile(r'[A-Za-z]')

# Open the input and output files
with open('book_names.txt', 'r', encoding="UTF-8") as infile, open('filtered_books.txt', 'w') as outfile:
    for line in infile:
        # Check if the line contains text characters
        if pattern.search(line):
            # Write the line to the output file
            outfile.write(line)

        

