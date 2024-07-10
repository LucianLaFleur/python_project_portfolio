from bs4 import BeautifulSoup as bs
import requests
target_output_name = "test_denton"
file_suffix = ".txt"
outfile_name = target_output_name + file_suffix

#  Variant structures: 
# 
# https://tvtropes.org/pmwiki/pmwiki.php/ComicStrip/NickKnatterton
# https://tvtropes.org/pmwiki/pmwiki.php/VideoGame/DeusEx
#  =======================================
# https://tvtropes.org/pmwiki/pmwiki.php/Main/OnlyInItForTheMoney
# https://tvtropes.org/pmwiki/pmwiki.php/Main/MadScientist
# target_list =["MadScientist"]



target_url_template = "https://tvtropes.org/pmwiki/pmwiki.php/"
target_suffix = "VideoGame/DeusEx"

full_target =target_url_template + target_suffix

def run_scrape(url):
    headers = {"Connection":"keep-alive",'User-Agent': 'Mozilla/5.0'}
    html_page = requests.get(url, headers=headers)
    soup = bs(html_page.text, "html.parser")
    article_div = soup.find('div', id='main-article')
    word_salad = article_div.get_text()

    with open(outfile_name, "w", encoding='utf-8') as my_file:
        my_file.write(word_salad)

run_scrape(full_target)

print(f"finished running, created file --> {outfile_name}")