#!/usr/bin/python3
def element_at(my_list, idx):
    if idx > (len(mylist) - 1):
        return "none\n"
    elif idx < 0:
        return "none\n"
    else:
        return mylist[idx]
