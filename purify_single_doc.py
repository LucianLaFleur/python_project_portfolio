import re

user_input_filename = input("enter a name for the output file >> ")

def filter_and_combine_files(filepath, filter_words, output_file):
    # Open the output file we're writing to...
    with open(output_file, 'w', encoding='utf-8') as out_file:
        # Open the target file we're reading from...
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                if not any(filter_word in line for filter_word in filter_words):
                    out_file.write(line)
        print(f"Finished purifying the document {filepath}")


# ----------------------------------------------

directory = './text_colle1'  

# words to exclude from the writing
filter_words = [ "[]", # remove anything containing braces in this pattern
    "Strange Part", "Released in Version", "CostStock", "Change History", " Released in Version", "TerminologyGeneral",
    "Quest Items", "This is a disambiguation page", "Turkish", "Menu Screenshot", "Hidden Exploration Objectives",
    "NPC", "locationAdditional", "(To be added.)", "QuestsThrough", "Mentioned Characters", "Unordered:", "Archon Quest", 
    "[1]", "VA", "Twitter", "Commission:", "World Quest", "Bilibili", "YouTube", "0D", "0E", "0W"] 
start_words = ["Old:", "Trivia", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Source", "Book Type"
               "A typo in", "Photo 1:", "Main article:"
            #    "↑", # links are made with this arrow symbol...
               ]  # List of words that should exclude a line if they appear at the start
# end_words = ["Quality", "Lore"]  # List of words that should exclude a line if they appear at the end
output_file = './' + user_input_filename + '.txt'  # The name of the output file

# PRESERVED
    # - version with ending-word exclusion too
# filter_and_combine_files(directory, filter_words, start_words, end_words, output_file)
filter_and_combine_files(directory, filter_words, start_words, output_file)

print("done!")