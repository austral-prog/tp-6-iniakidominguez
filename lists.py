def remove_elements(lst):
    lst_copy = lst[:]
    for i in sorted([0, 4, 5], reverse=True):
        if i < len(lst_copy):
            del lst_copy[i]
    return lst_copy

def add_elements(lst):
    return ['Pink'] + lst + ['Yellow']

def is_empty(lst):
    return len(lst) == 0

def check_lists(lst1, lst2):
    if len(lst1) > 2 and len(lst2) > 2:
        return lst1[2] == lst2[2]
    return False

def list_of_lists(list_of_lists_to_modify):
    return [
        list_of_lists_to_modify[0][:2],
        list_of_lists_to_modify[1][1:4],
        list_of_lists_to_modify[2][-2:]
    ]
