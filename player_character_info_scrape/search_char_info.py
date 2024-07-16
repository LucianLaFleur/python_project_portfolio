import os
import re
import glob

def find_matches_in_files(directory, search_word, output_file):
    # Escape the search word to handle any special regex characters
        # This lets us add a variable into the regex pattern, which we pass into the function via search_word
    escaped_search_word = re.escape(search_word)
    # The search-word still needs to be compiled into a pattern for regex to match
    regex_pattern = rf'(?i)\b{escaped_search_word}\b|\b{escaped_search_word}'
    pattern = re.compile(regex_pattern)

    # Open the output file in write mode
    with open(output_file, 'w', encoding='utf-8') as out_file:
        # Walk through the directory and all subdirectories
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.txt'):
                    filepath = os.path.join(root, file)
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()

                        # Find all matches of the pattern in the content
                        matches = pattern.finditer(content)

                        for match in matches:
                            # Note, second argument shows the limit, so start index is match - 50 or 0, whichever is bigger (because max())
                            start_index = max(match.start() - 80, 0)
                            #opposite pattern for min, match + 80 or content length, whichever is smaller because of min()
                            end_index = min(match.end() + 80, len(content))
                            # check for \n after match, and terminate the amount of chars returned if newline gets detected
                            # newline_index = content.find('\n', match.end())
                            # if newline_index != -1 and newline_index < end_index:
                            #     end_index = newline_index

                            context = content[start_index:end_index]

                            # Write the match and its context to the output file
                            out_file.write(f"{os.path.basename(filepath)}:\n ")
                            out_file.write(f"{context}\n")

# ----------------------------------------------------------------------------------------------------------------------------------------

target_string = input("input a word or word-fragment to match: ")
# Match "under" as part of any longer string 
#       - will match ANY occurrence of "under", like "blunder" or "sunder".

# To restrict to starting portion only...
# r'(?i)\bunder\b|\bunder'
#   - (?i): Makes the pattern case-insensitive.
#   - \b: Word boundary. This ensures that "under" is matched as a whole word 
# and not as part of a longer word unless it's followed by another word character.
# under: The word "under".
#   - \bunder: This part ensures that if "under" is part of a longer word (e.g., "undertake"), it is still matched.
# The above pattern covers both standalone "under" and words starting with "under" (like "undertake").    

directory = 'purified_char_data'  # Specify the directory containing the text files we want to iterate through...
output_file = 'zz_' + target_string + '_results.txt'

find_matches_in_files(directory, target_string, output_file)

print(f"output file {output_file} created!")
