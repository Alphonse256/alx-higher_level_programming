#!/usr/bin/python3
# delete_at - Deleted element at a specific index

def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    else:
        my_list.pop(idx)
        return my_list
