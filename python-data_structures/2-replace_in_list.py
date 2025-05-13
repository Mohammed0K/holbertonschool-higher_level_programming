#!/usr/bin/python3
def replace_in_list(my_list, idx, new_element):
    my_list[idx] = new_element
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
