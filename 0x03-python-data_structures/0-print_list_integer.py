#!/usr/bin/python3
# print_list_integers - Prints the list of integers each on a newline
def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
