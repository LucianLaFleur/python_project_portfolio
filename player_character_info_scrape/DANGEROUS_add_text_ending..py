import os
def add_txt_extension_to_files(directory, extension):
    # Iterate through all files in the specified directory
    for filename in os.listdir(directory):
        # Construct the full file path
        filepath = os.path.join(directory, filename)
        
        # Check if it is a file (not a directory) to manipulate
        if os.path.isfile(filepath):
        #  PRESERVED
            # needed to get rid of ending so sliced off mistaken add
            # new_filepath = filepath[:-13] + extension
            new_filepath = filepath + extension
            os.rename(filepath, new_filepath)
            # print(f"Renamed: {filename} to {filename}extension")

# Process execution ---------------------------------

add_txt_extension_to_files('.', '.txt')  # period for the current directory

print("done 002")