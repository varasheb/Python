# 8. Write a Python program to remove an item from a tuple.


def remove_item(my_tuple, item_to_remove):
    new_tuple = tuple(item for item in my_tuple if item != item_to_remove)
    return new_tuple

def main():
    my_tuple = (1, 2, 3, 4, 5)
    item_to_remove = 3
    new_tuple = remove_item(my_tuple, item_to_remove)
    print("Tuple after removing item", item_to_remove, ":", new_tuple)

main()
