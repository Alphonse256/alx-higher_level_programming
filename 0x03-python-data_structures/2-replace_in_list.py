#!/usr/bin/python3
# replace_in_list - Replaces an item at a specified idx
def replace_in_list(my_list, idx, element):
    length = len(my_list) - 1
    if idx < 0 or idx > length:
        return (my_list)
    else:
        my_list[idx] = element
        return (my_list)
