#  Dev-log, 
# 
# for scraping the English genshin wiki: several tabs are targets for the characters, 
# 
# moved away from having several arrays then using a counter to track names
# name_arr = ["alice", "bob", "charlie"]
# arr1 = ["alice/link1", "bob/link1", "charlie/link1"]
# arr2 = ["alice/link2", "bob/link2", "charlie/link2"]
# --- invocation 
# idx_counter = 0
# for x in name_arr:
    # my_function(name_arr[idx_counter])
    # my_function(arr1[idx_counter])
    # my_function(arr2[idx_counter])
    # ...

#  Refactored ---->
# master_arr = [
# ["alice", "alice/link1", "alice/link2"], 
# ["bob", "bob/link1", "bob/link2"],
# ["charlie", "charlie/link1", "charlie/link2"]
# ]
# -- invocation becomes MUCH cleaner
# for sub_arr in master_arr:
    # for item in sub_arr:
        # my_function(item)