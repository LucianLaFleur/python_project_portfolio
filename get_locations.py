

# need to grab all names of locations and points of interest....
# # Find the target div
# target_div = soup.find('div', class_='mw-parser-output')

# # Initialize a list to hold the text content of <p> tags
# paragraphs = []

# # Iterate over the children of the target div
# for child in target_div.children:
#     if child.name == 'div':
#         break  # Stop iterating if a <div> is encountered
#     if child.name == 'p':
#         paragraphs.append(child.get_text())

# # Print the collected paragraphs
# for paragraph in paragraphs:
#     print(paragraph)