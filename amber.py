import sys
from bs4 import BeautifulSoup as bs
import requests
import os
import re
# -*- coding: utf-8 -*-

# ! NOTE: not a target, since we're using the principle of contrast to 
# enhance short, memorable phrases. Synonyms tend to confuse learners when presented together.
 
# NOTE: Antonyms are a key target, and should be integrated into examples, 
  # use appropriate grammar and lean towards portraying context with antonyms or thematically consistent ideas
 

keywords = ["Antonyme", "Verwendungsbeispielsätze", "Phraseologismen"]

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

def run_the_scrape(url):
  headers = {"Connection":"keep-alive",'User-Agent': 'Mozilla/5.0'}
  html_page = requests.get(url, headers=headers)
  soup = bs(html_page.text, "html.parser")
  # Cutting down on the entire soup...
  # First, find the <div> tag with the id "mw-content-text"
  content_div = soup.find('div', id='mw-content-text')
  # Iterate over the keywords to find the corresponding <p> tags (the fake-headers),
  #  which may be absent
  for keyword in keywords:
      # Find the <p> tag with the specified keyword in the title attribute
      p_tag = content_div.find('p', title=keyword)
      # If the <p> tag is found, find the immediate sibling <dl> tag
      if p_tag and p_tag.find_next_sibling('dl'):
          phrases_dl = p_tag.find_next_sibling('dl')
          
          # Find all <dd> tags within the phrases_dl
          dd_tags = phrases_dl.find_all('dd')
          
          # Print the text content of each <dd> tag
          for dd in dd_tags:
              print(dd.get_text())

  # # Print the text content of each <dd> tag
  # for dd in dd_tags:
  #     print(dd.get_text())

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

while True:
  url = input("paste a url to scan: ")
  if url == "c":
   break
  else:
    run_the_scrape(url)


# Beispiele
# Redewendungen
# Wortkombinationen
  
# print("Reminder crtl+w closes current tab")

# scan_gifcount(lops)

# https://e-hentai.org/?f_cats=967&f_search=animated&advsearch=1&f_srdd=4

# https://e-hentai.org/g/2972218/444be4d05e/

# https://e-hentai.org/g/2972218/444be4d05e/
#  (skyrim animated?)
# https://en.wikiquote.org/wiki/German_proverbs

# Target: scrape all words from all German voice lines in Genshin, honkai star rail
# https://genshin-impact.fandom.com/de/wiki/Amber/Stimme lines done in german, 
# take the voices, use AI to generate them in German to add to flashcards

#  
# https://de.wiktionary.org/wiki/abhalten
# 
# on cli, get the pattern to print out the examples, and since these jerks don't have it translated, do so with the espada.

# mw-content-text
#  <div>
        # 
# Using python and Beautiful Soup to look at a web-page I am making, I need to navigate the DOM with Beautiful Soup to get some particular fields. There is a tag I'm not familiar with `<dl>` which contains the information I want to grab. 
# The structure to find the target <dl> tag is as follows: find the <div> containing the id "mw-content-text", then find the first child <div>, then find the sixth <dl> tag. Inside the <dl> tag, there may be a different number of child elements, each of which will consistently be within <dd> tags. My goal is to print the text content of each of these DD tags to the screen. (assume I'm just running python from the command line)

# Your code is correct, but I need to change what text I am targeting due to inconsistencies in format. I cannot expect the content to be in the same position by counting the <dl> tags. Instead, I need to look over the page to find three possible keywords in the "title" part of a <p> tag. These keywords are "example", "opposite", and "phrases". The structure would be like `<p title=phrases>These are the phrases spoken by this famous person<p>` 
# If this is found, I'll save it to a variable called something like "phrases_p"
# Then, I just need to find the first sibling element to each of these <p> tags, which should be a <dl> following immediately after them. Continuing our naming convention, this would be "phrases_dl".  Then, we can reuse the same logic `dd_tags = phrases_dl.find_all('dd')
# for dd in dd_tags:
#       print(dd.get_text())`