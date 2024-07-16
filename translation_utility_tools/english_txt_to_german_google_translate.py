from datetime import datetime
from googletrans import Translator
import time

# Static values here can change and will be reflected in the UI
eng_file_name = input("input filename (without.txt) here >> ")
eng_only_sentence_file = f"{eng_file_name}.txt"
# timestamp and .txt will be added to tsv below
tsv_name = f"german_{eng_file_name}"

# unformatted, lame time object
raw_time = datetime.now()
# format current time into hours, minutes, seconds
formatted_hms_current_time = raw_time.strftime("%Hh%Mm%Ss")

# Basic utility function for extracting .txt file lines as array items
def read_sentences_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        sentences = [line.strip() for line in file]
    return sentences
# ASCII Progress Bar
def print_progress_bar(iteration, total, prefix='', length=30, fill='#'):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} [{bar}] {percent}% Complete\n', end='', flush=True)
# Translator functionality, extracted for berevity
def translate_text(text, target_language='de'):
    translator = Translator()
    result = translator.translate(text, dest=target_language)
    return text, result.text
# Translate the English-only into a target language, defaulting to Spanish
def translate_eng_sentences(eng_only_input_file_path):
    # Read sentences from the file
    sentences = read_sentences_from_file(eng_only_input_file_path)
    # Translate and collect the results
    results = []
    total_sentences = len(sentences)
    for i, sentence in enumerate(sentences):
        # input(f"sentence is >> {sentence}")
        print("sleeping for 3 seconds to chill")
        time.sleep(0.5)
        original, translated = translate_text(sentence, "de")
        results.append(translated + '\n')
        results.append(original + '\n')
        results.append(' \n')
        print(f"{original} -> {translated}")
        print_progress_bar(i + 1, total_sentences)
    # print(results)
    # input("checking results output ^^ ---- 01")
    return results
#  Extract the target sentences for analysis
def get_target_only_sentences(array_of_duo_translations):
    translated_sentences = array_of_duo_translations[0::3]
    translated_sentences = [sentence.strip() for sentence in translated_sentences]
    return translated_sentences
# Make the sentence-pairs into a TSV format (tab separations for Anki to understand)
def tsv_format_translation_pairs(in_list):
    # Delete every 3rd item, getting rid of the space-separators
    in_list = [item for index, item in enumerate(in_list) if (index + 1) % 3 != 0]
    out_list = []
    # print(in_list)
    for index in range(0, len(in_list), 2):
        odd_item = in_list[index].strip() + "\t"
        even_item = in_list[index + 1].strip() + "\t\t\t"
        combined_string = odd_item + even_item + "\n"
        out_list.append(combined_string)
    return out_list
#  Identify all individual words used across all sentences

#  Big, bad process execution
def process_documents():
    # Below globals are just used for file-names
    global formatted_hms_current_time
    global eng_only_sentence_file
    global tsv_name

    # Actually translate the sentences
    translated_arr = translate_eng_sentences(eng_only_sentence_file)

#[!] filename for translations (language key portion) changes depending on dropdown string selected in UI
    with open("z_german_translated_sentences_" + formatted_hms_current_time + ".txt", 'w', encoding='utf-8') as translated_sentences_duo_document:
        for item in translated_arr:
            translated_sentences_duo_document.write(item)
            
    # Prepare the translated sentences in a TSV format for Anki importing
    tsv_array = tsv_format_translation_pairs(translated_arr)
    # Write out the tsv document
    with open(tsv_name + formatted_hms_current_time + ".tsv", 'w', encoding='utf-8') as my_tsv_doc:
        for tabby_line in tsv_array:
            my_tsv_doc.write(tabby_line)

process_documents()
