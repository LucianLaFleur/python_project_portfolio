unfinished documentation
[NYI] - purpose document for TV trope single-shot scraper
[NYI] - purpose document for Genshin text project

==== unfinished programs (general)

[!] - The german Genshin scraper is very messy currently and needs to have files cleaned and consolidated
    - Need to make the german scraper for German voice line text

[!] - the TV_Tropes text-grabber and power-shell searcher is messy and needs files consolidated in a new directory

==== unfinished in dndAutomations DIR

"magic chaos" is a wild magic generator. The logic changes a ton based off effects. (journal NYI, but I will make a changelog as I develop it further)

"Wild magic dictionary" is a bunch of reference dictionaries and arrays to make "magic chaos" work.
Statistics and balance will be found here.

====================================================================================================
==== functional programs
====================================================================================================

file "chaos bolt" is Rules-as-written, automating the 1d8 table.
This makes multiple chains very unlikely.

file "custom chaos bolt" makes a flat 1/3 chance (instead of 1/8) for chained damage or effects, adding variation to tactics because you can declare a debuff or straight damage
(descriptions explain how backfires work and give a better feel of "more power = more danger" as an embodiment of chaos)

file "rand polymorph" is for testing the randomized polymorph dictionary. This is a set of CR1 appropriate monsters as an attempt at stat balance. 
NOTE: The dictionary is ordered from useless to powerful, but not broken. A Giant Spider is overly strong for a lvl1 spell, but it balances out, given that you, or an enemy, could turn either into that or a slug.
[probably should be play-tested as it's own variation lvl-1 spell slot, bonus-action cast, like a sorcerer not having control to contrast from a druid's discipline]

====================================================================================================

Devlog:

11 July 
# 11 July log:
Spider ran across 2900+ npc files, text gathered successfully!
Checking on files, deleting a few that have no meaningful content text... there's no consistent way to check for the "usefulness" systematically, since it's subjective. It's all just a reference source for powershell anyway. 
    (not yet doing the powershell stuff since there's more to scrape with the "food" descriptions)
Made food_name_grabber.py to get all 300+ food names, removing duplicates, and output to a textfile
    targeting for food names irregular, multiple failures eats up time... but I persist and now for the correct output file.
    UTF-8 is needed for the names in links, so saving to a text file in UTF-8 also helps with encoding characters like dashes and apostrophies in the url names with their % calls.

10 July: 
<!-- Remember: only single-requests are done to a given page at a given time. Limit all batch sizes to not overwhelm the wiki site! -->
    For English Genshin scraper:
        identified and documented a new pattern for the spider to crawl to interesting portions:
        The goal is, for each character, get the following
        1) Details from a particular portion of the character's main page (the rest of text outside of this particular <p> tag is irrelevant)
        2) make a master list comprised of sub-arrays containing the character-specific URLs for main, lore, outfits, companion, and voice-overs.
        3) Write functions to handle extracting the interesting info from each page.
    In-progress:
    Making an ad-hoc grabber for the content of each interesting url, as the content structure is a little irregular with the id's used to identify the main text-containing areas.
        - The ad-hoc grabber is a function that tries just one of the URLs from the sub-array. Since the structures of HTML on the target pages are different, I need to test them individually. Then I can write functions for each to see if they return the content I'm looking for. 
    
    [!] Complexity discovered:
        - The "outfits" portion will list the character's different outfits in a table. This requires another scraping script to grab, and then that gives more links to follow.
        - Outfits lead to nested data, which is valuable because visual descriptions are high-quality for vocabulary, plus ALL of them have a visual to accompany them, making this info ideal for flashcards, should a match arise on vocab words down the line.

9 july:
    Begin analyzing html for both German and English Genshin wiki website.
        Identified url pattern and key subdirectories with interesting information (for example sentences)
    Wrote program to collect all character names and output in textfile (84 main character names in underscored_genshin_names.txt)
        - basic testing showed spaces convert to underscored for URLs I want to navigate through using these names...
    Wrote npc name grabber:
        - goes through the page listing all NPC's, collected over 1000 names
    wrote text_from_npc_profiles --> 
        - using NPC names, get the text information on the page about them
        - each NPC page gets its own .txt file, using the npc's name as the file name, followed by "_word_salad.txt"
    wrote powershell script to look through textfiles of npc content (if they're all in a targeted subdirectory as indicated by the code)
        - can find keywords in English and output a number of characters before and after (adjustable in the "match" portion of the .ps1 file)

    *for GERMAN version of Genshin Scraper, program made to scrape all data from main pages
        - all the GERMAN text data from each character's main page is collected in main_page_textfiles.
    Begin development on a single-page TV tropes scraper (currently looking solely at getting data from the Video Games category)
        - can extract text data
        - Secondary powershell program made, can search for characters before and after a hit on a keyword: DeusEx page's text data, 
    *Expand 

8 july: 
- make dev journal for magic chaos
- polymorph dictionary added, and effect of random polymorph added (needs testing)
    - to-do [confirm polymorph randomization gets the data from the dictionary correctly]
chaos bolt works with several random effects, confirmed for straight damage and damage + effect, balanced based on effect type
Damage type randomized fairly
1/8 chance for declared damage or effect cast to be inverted 


7 july: working on DnD tools for calculating random wild-magic effects and automatically rolling to resolve outcomes.
