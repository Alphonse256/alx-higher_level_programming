#!/usr/bin/python3
# divisible_by_2 - Returns the multiples of 2

def divisible_by_2(my_list=[]):
    multiples = []
    for number in my_list:
        if number % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)
    return multiples
