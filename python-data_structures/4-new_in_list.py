#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        a = my_list.copy()
        if idx < 0 or idx >= len(my_list):
            return a
        else:
            a[idx] = element
            return a
