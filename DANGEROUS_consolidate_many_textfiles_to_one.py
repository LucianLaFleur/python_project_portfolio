import os
import re

# -------------------

                                #  - end pattern removed from input params
def filter_and_combine_files(directory, filter_words, start_words, output_file):
    # Compile regex patterns for start and end words
    start_patterns = [re.compile(rf'^{re.escape(word)}\b', re.IGNORECASE) for word in start_words]

    #  - end patterns not used
    # end_patterns = [re.compile(rf'\b{re.escape(word)}$', re.IGNORECASE) for word in end_words]
    counter = 0
    # Open the output file in write mode
    with open(output_file, 'w', encoding='utf-8') as out_file:
        # Iterate through all files in the specified directory
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            counter += 1
            if counter == 5550:
                print("5550 items reached! breaking for safety")
                break
              # Check if it's a file, not a DIR
            if os.path.isfile(filepath) and filepath.endswith('.txt'):
                with open(filepath, 'r', encoding='utf-8') as f:
                    for line in f:
                        # Check if the line is less than 24 characters long, skip if so
                        if len(line) < 23:
                            continue
                        # Skip the line if it matches any of the start patterns
                        if any(pattern.match(line) for pattern in start_patterns):
                            continue
                    # - unused 
                        # Skip the line if it matches any of the end patterns
                        # if any(pattern.search(line) for pattern in end_patterns):
                        #     continue

                        # Finally, if none of the filter words are in the line, write the line to the output file
                        if not any(filter_word in line for filter_word in filter_words):
                            out_file.write(line)
                print(f"Finished with {filepath}, #{counter}")

# ----------------------------------------------------------------------------------------------------------------
directory = './text_colle1'  

# words to exclude from the writing
filter_words = [ "[]", # remove anything containing braces in this pattern
    "Strange Part", "Released in Version", "CostStock", "Change History", " Released in Version", "TerminologyGeneral",
    "Quest Items", "This is a disambiguation page", "Turkish", "Menu Screenshot", "Hidden Exploration Objectives",
    "NPC", "locationAdditional", "(To be added.)", "QuestsThrough", "Mentioned Characters", "Unordered:", "Archon Quest", 
    "[1]", "VA", "Twitter", "Commission:", "World Quest", "Bilibili", "YouTube", "0D", "0E", "0W", "0)", "5)", "Recipes:", 
    "Recipe:"] 
start_words = ["Old:", "Trivia", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Source", "Book Type"
               "A typo in", "Photo 1:", "Main article:"
            #    "↑", # links are made with this arrow symbol...
               ]  # List of words that should exclude a line if they appear at the start
# end_words = ["Quality", "Lore"]  # List of words that should exclude a line if they appear at the end
output_file = './combined_output.txt'  # The name of the output file

# PRESERVED
    # - version with ending-word exclusion too
# filter_and_combine_files(directory, filter_words, start_words, end_words, output_file)
filter_and_combine_files(directory, filter_words, start_words, output_file)

print("done?")

# kill words "Realm Depot", "Elemental Burst", "Main article:"