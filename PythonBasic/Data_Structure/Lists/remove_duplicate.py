# 6. Write a Python program to remove duplicates from a list.

def remove_duplicates(items):
    unique_items = []
    for item in items:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items

def main():
    items = [1, 2, 3, 2, 4, 5, 6, 4]
    print("List after removing duplicates:", remove_duplicates(items))


main()
