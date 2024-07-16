# intended use
# Expected pattern:
    # German
    # English
    # [blank space]
# ^ above 3 line structure repeating across a text file, eg:
#                   -------------
    #  SAMPLE AS IF FROM .TXT FILE
#                   -------------
# Das Feuerwerk war beeindruckend.
# The fireworks were impressive.

# In dem Vertrag wurden die Details genau festgelegt.
# The details were stipulated precisely in the contract.

# Ich bevorzuge Kaffee vor Tee am Morgen.
# I prefer coffee over tea in the morning.
#                   -------------

# Output becomes TSV in a format for my ANKI cards.
# - assumes 4 fields exist, with the first 2 as GERMAN, ENGLISH
    # - other fields are "audio" and "pic", which are not handled in this program

# Example output
# Wir sprechen später.\tTalk to you later.\t\t\t
# Ich komme später wieder.\tI'll be back later.\t\t\t		
# Wird es morgen regnen?\tWill it rain tomorrow?\t\t\t
# NOTE: ^^^ above, the \t is written so you can visualize the whitespace
        #  in an actual output .txt file, this will be whitespace and not directly visible as the special characters
        #  also note the newline pattern, which is expected so as to be read by the TSV function on ANKI (which looks at the input file line-by-line)

def process_lines(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        lines = infile.readlines()
        
        # Process lines in chunks of 3 (German, English, blank)
        for i in range(0, len(lines), 3):
            german = lines[i].strip()  # German line
            english = lines[i + 1].strip()  # English line
            
            # Write the output in the desired format
            outfile.write(f"{german}\t{english}\t\t\t\n")

# Specify the input and output file paths
input_file = 'german_sentence_pairs_7_14_coolness.txt'
output_file = 'german_tsv_002.txt'

# Process the file
process_lines(input_file, output_file)
print(f"processing {output_file} complete!")
