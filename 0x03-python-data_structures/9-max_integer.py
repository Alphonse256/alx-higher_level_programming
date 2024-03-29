#!/usr/bin/python3
# max_integer - Finds the largest number in a list

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    max_number = my_list[0]
    for num in my_list:
        if num > max_number:
            max_number = num
    return (max_number)
