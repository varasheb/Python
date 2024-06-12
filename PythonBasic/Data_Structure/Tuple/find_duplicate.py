# 5. Write a Python program to find the repeated items of a tuple.

def find_repeated_items(my_tuple):
    repeated_items = []
    for item in my_tuple:
        if my_tuple.count(item) > 1 and item not in repeated_items:
            repeated_items.append(item)
    return repeated_items

def main():
    my_tuple = (1, 2, 2, 3, 4, 4, 5)
    repeated_items = find_repeated_items(my_tuple)
    print("Repeated items:", repeated_items)

main()
