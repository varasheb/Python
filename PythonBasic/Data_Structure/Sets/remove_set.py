# 4. Write a Python program to remove item(s) from set
# 5. Write a Python program to remove an item from a set if it is present in the set.

def remove_items(s, items):
    new_set = set()
    for item in s:
        if item not in items:
            new_set.add(item)
    return new_set

def remove_if_present(s, item):
    new_set = set()
    found = False
    for i in s:
        if i == item and not found:
            found = True
        else:
            new_set.add(i)
    return new_set

def main():
    my_set = {1, 2, 3, 4, 5}
    items_to_remove = {2, 4}
    my_set = remove_items(my_set, items_to_remove)
    print("Set after removing items:", my_set)
    
    
    my_set = {1, 2, 3, 4, 5}
    item_to_remove = 4
    my_set = remove_if_present(my_set, item_to_remove)
    print("Set after removing item if present:", my_set)
    
main()