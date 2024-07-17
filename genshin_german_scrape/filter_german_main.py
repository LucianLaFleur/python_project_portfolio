import os
# -------------------
def filter_and_combine_files(directory, filter_words, output_file):
    counter = 0
    # Open the output file in write mode
    with open(output_file, 'w', encoding='utf-8') as out_file:
        # Iterate through all files in the specified directory
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            counter += 1
            if counter == 555:
                print("555 items reached! breaking for safety")
                break
              # Check if it's a file, not a DIR
            if os.path.isfile(filepath) and filepath.endswith('.txt'):
                with open(filepath, 'r', encoding='utf-8') as f:
                    for line in f:
                        # Check if the line is less than 25 characters long, skip if so
                        if len(line) < 25:
                            continue
                        # If none of the filter words are in the line, write the line to the output file
                        if not any(filter_word in line for filter_word in filter_words):
                            out_file.write(line)
                print(f"Finished with {filepath}, #{counter}")

# ----------------------------------------------------------------------------------------------------------------
directory = './main_page_textfiles'  

# words to exclude from the writing
filter_words = [ "[]", "↑", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Datei:",
                "}", "•", "figuren", "Figuren", "materialien", "Text wird", "Chinesisch(traditionell)"] 

output_file = './filtered_main_DE_articles4.txt'  # The name of the output file

filter_and_combine_files(directory, filter_words, output_file)

print("file filter complete")
