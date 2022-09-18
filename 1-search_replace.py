#!/usr/bin/python3


def search_replace(my_list, search, replace):
    if my_list is None:
        return

    new_list = [replace if switch == search else switch for switch in my_list]
    return new_list