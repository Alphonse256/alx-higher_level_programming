#!/usr/bin/python3
# element_at - Prints a number at a specified index
def element_at(my_list, idx):
    length = len(my_list)
    if idx < 0:
        return None
    if idx > length:
        return None
    else:
        return my_list[idx]
