from bs4 import BeautifulSoup as bs
import requests
# define static name for url and output;
# target input is a single, static page
# Target output is a list of names scraped from the page

url = "https://genshin-impact.fandom.com/wiki/Character/List"
file_name = "underscored_genshin_names.txt"

def scrape_names():
    names_list = []
    # init the names list that we ultimately want for the output
    headers = {"Connection":"keep-alive",'User-Agent': 'Mozilla/5.0'}
    html_page = requests.get(url, headers=headers)
    soup = bs(html_page.text, "html.parser")
#    get the first <tbody> tag appearing on the page
    my_tbody = soup.find('tbody')
    my_trows = my_tbody.find_all('tr')
    # ignore the first table row because it's the title row, not actual data
    for table_row in my_trows[1:]:
        my_tdata = table_row.find_all('td')
        
    # PRESERVED TO SHOW DEV. PROCESS
        # # Diagnose where the data for the name can actually be extracted
        # print(my_tdata[1].get_text())
        # # control the output to pause after showing one item at a time...
        # input("continue?")

    #  from out diagnostic, we know `my_tdata[1].get_text()`` will return the name
    #       Now, we can append that to out output list
        names_list.append(my_tdata[1].get_text())
    
    # outside of loop below...
    return names_list

#  Process execution -----------------------------------------------------------------

all_names = scrape_names()
space_bearing_names = 0
with open(file_name, "w") as outfile:
    for item in all_names:
        if " " in item:
            print(f"Space detected in {item}")
            underscored_item = item.replace(" ", "_")
            print(f"Changed to --> {underscored_item}")
            outfile.write(underscored_item)
            space_bearing_names += 1
        else:
            outfile.write(item)
print(f"=" * 33)
print(f"{space_bearing_names} names had spaces replaced with underscores")
print(f"{file_name} created!")

