Task Kanban
[DEV] - Character scraper
[Research] - Find  
[DEV] - Nation spider -> lore. history, etc, needs to crawl
[DEV] - german wiki scraper, Stimme
[LOG] - purpose document for TV trope single-shot scraper
[LOG] - purpose document for Genshin text project
[ORG] - copy all source text files into a shared collection folder to make it easier to scan in powershell
[CK] - CHECK sub-folders for their own purpose documents, tracking documentation
[CK] - check completed code for PRESERVED keyword, so as to add notes to the associated documentation
[LOG] - document the npc info scraper
[LOG] - document the food scraper
--- very low priority
[dev] - english to X script, based off images of characters... (https://genshin-impact.fandom.com/wiki/Language#English)

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

=========================================
Concerning the Genshin Wiki info scrapers
=========================================
Overview of process:
Generally, needed to find a collection of item names, 
    e.g. all character names/food items/weapons, 
    Then, find a pattern for the url pages containing descriptive text.
    - usually [root wiki url] + /item_name
The names are a means to an end of collecting this list of urls.
    - Then, go through each target URL and extract descriptive text
    - The location of descriptive text changes depending on the article structure.
        - e.g. Food has a bunch of irrelevant stat info, so only a particular <div> has the target text.
        However, other things like furnishings sometimes have associated text-tables containing useful dialogue, but not always.
        - The variance in patterns really demanded a lot of personal judgment to deem what info was worth grabbing and where.

=========================================
in dndAutomations
=========================================

file "chaos bolt" is Rules-as-written, automating the 1d8 table.
This makes multiple chains very unlikely.

file "custom chaos bolt" makes a flat 1/3 chance (instead of 1/8) for chained damage or effects, adding variation to tactics because you can declare a debuff or straight damage
(descriptions explain how backfires work and give a better feel of "more power = more danger" as an embodiment of chaos)

file "rand polymorph" is for testing the randomized polymorph dictionary. This is a set of CR1 appropriate monsters as an attempt at stat balance. 
NOTE: The dictionary is ordered from useless to powerful, but not broken. A Giant Spider is overly strong for a lvl1 spell, but it balances out, given that you, or an enemy, could turn either into that or a slug.
[probably should be play-tested as it's own variation lvl-1 spell slot, bonus-action cast, like a sorcerer not having control to contrast from a druid's discipline]

====================================================================================================

Devlog:

12 July:
Finish food description spider (successful .txt file creation in ./food_descriptions)
    - needed to make exceptions for targets that did not lead to a valid link, and thus returned no text
    - program correctly ignored bad link-nams with try-except block (could diagnose mistakenly-listed items this way if managing a database of my own)

genshin_scrape_common_functions.py made 
    - contains reusable functions for 1) randomizing a float for sleep-time 2) getting all text content from a common id found in most articles
[Refactoring] Technically, with the common-functions file, I could go back and clean up other files, but given they've already served their purpose and grabbed data from running, this is irrelevant. Deemed a poor use of time to refactor when the programs will not be used again. However, since "get_weapon_info.py" is in development, I will use it there.

Significant HTML investigation has identified the following areas of interest for text content:
    quest Unit
    quest chapter names (dialogue, priority)
    weapon descriptions
    furnishings
    imaginarium voice-overs
    imaginarium fortune-slips
    (all of the above have significant text-content targets)

Collected quest units, separated from quest chapters (different structure for URL, since suffix /story needs to be added to the unit names);
    A quest unit is like a collection of quest chapters.
    No HTML markers identified the units apart from chapters, and the articles themselvs suffered from repeats and inconsistent structure so ad hoc sorting was necessary
Removed the chapter-headings from quest chapters:
    ex: part1: my chapter name --> my_chapter_name
    (needed to remove headers like part1, since those weren't in the url, then exchange underscores for spaces.)

    name and content extractors made for furnishing data
    Modified extractors for furnishing data to extract weapon data, though several differences documented
        -->  Error encountered and resolved:
        #  each string iterated over and then printing one char each on a line. 
        #  check the loop where the text data is being written for output to remove this problematic iteration. Check where the newline     character is being added to.
        # resolution ---> iteration removed from output processing, since the strings were treated as arrays, adding a newline after each character. Removed iteration structure.

        Differences for weapon extractor:
        -   Instead of returning the element, like we have to in the list of elements in the furnishing descriptions, we return the text for the main article's content
        -   Instead of iterating over an array of tags to extract data and then append the text output, we directly have the article content as text already, thus, we only have to add the page title : text content.
        - Pattern should apply to hangouts section...

    name and content extractors made for hangout data
        - (minimal changes from weapon extractor, though needed to extract and process ad-hoc headings being different from url endings...)

Miscilanous main content extractor made: collected multiple urls which all had similar content structures.
    - various forms of iteration applied to the different patterns (like countries each having culture, design, and history to them)
    - quest header summaries collected from text file, then each read and added url suffix "/Story" to the name to get the target url
    - some single-pages added where large amounts of content were in the imaginarium's fortune slips and voice-overs sections
    - missed the arataki-related urls, manually added as well

Make book_name_collector.py to get all names. Interesting need to exclude spaces and number-only lines so that I can filter out garbage info to get the titles for urls quickly.

[!] updated common functions with remove_lines_lacking_letters(infile, outfile)
    - Takes in a textfile, outputs a text file with only lines that contain letters as info.
    - This way, dumb info that only has numbers or is empty spaces will get removed, improving data quality

[!] Added an array to catch any problematic urls and continue on the processing so the miscelanous data can be gathered and exceptions singled out.
    - Very good diagnostic practice, and no re-treading ground with a bunch of exceptions in the content-grabber.

11 July 
# 11 July log:
Spider ran across 2900+ npc files, text gathered successfully!
Checking on files, deleting a few that have no meaningful content text... there's no consistent way to check for the "usefulness" systematically, since it's subjective. It's all just a reference source for powershell anyway. 
    (not yet doing the powershell stuff since there's more to scrape with the "food" descriptions)
Made food_name_grabber.py to get all 300+ food names, removing duplicates, and output to a textfile
    targeting for food names irregular, multiple failures eats up time... but I persist and now for the correct output file.
    UTF-8 is needed for the names in links, so saving to a text file in UTF-8 also helps with encoding characters like dashes and apostrophies in the url names with their % calls.
[+] Formatted output of all food descriptions as "name: description" so it's one file with a lot of data. This will help comparing performance with powershell scripts.

10 July: 
<!-- Remember: only single-requests are done to a given page at a given time. Limit all batch sizes to not overwhelm the wiki site! -->
    For English Genshin scraper:
        identified and documented a new pattern for the spider to crawl to interesting portions:
        The goal is, for each character, get the following
        1) Details from a particular portion of the character's main page (the rest of text outside of this particular <p> tag is irrelevant)
        2) make a master list comprised of sub-arrays containing the character-specific URLs for main, lore, outfits, companion, and voice-overs.
        3) Write functions to handle extracting the interesting info from each page.
    Small program for removing duplicate names created remove_dupe_names.py
        - Correctly gets rid of duplicates, demonstrating using the builtin function set() to find unique items out of a list quickly. 
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
