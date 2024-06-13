# 11. Write a Python program to convert a list into a nested dictionary of keys.

def list_to_nested_dict(lst):
    nested_dict = current = {}
    for key in lst:
        current[key] = {}
        current = current[key]
    return nested_dict

def main():
    lst = ['a', 'b', 'c', 'd']
    result = list_to_nested_dict(lst)
    print("Nested Dictionary:", result)

main()