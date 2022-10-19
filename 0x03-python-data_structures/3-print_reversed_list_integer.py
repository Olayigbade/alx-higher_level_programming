#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    else:
        index = len(my_list) - 1
        while index >= 0:
            print("{:d}".format(my_list[index]))
            index -= 1
