import bisect


def insert_to_sorted_list(lst, new_item):
    bisect.insort(lst, new_item)
    
    return lst

