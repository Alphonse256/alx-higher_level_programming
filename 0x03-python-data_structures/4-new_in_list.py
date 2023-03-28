#!/usr/bin/python3
# new_in_list - Copies a list of items
def new_in_list(my_list, idx, element):
    length = len(my_list) - 1
    if not(idx < 0 or idx > length):
        nw_list = my_list.copy()
        nw_list[idx] = element
        return (nw_list)
    return (my_list)
