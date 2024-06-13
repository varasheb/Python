# 13. Write a Python program to count number of items in a dictionary value that is a list.


def count_list_items(d):
    count = 0
    for value in d.values():
        if isinstance(value, list):
            count += len(value)
    return count

def main():
    sample_dict = {'a': [1, 2, 3], 'b': [4, 5], 'c': 6}
    result = count_list_items(sample_dict)
    print("Total number of items in lists:", result)
    
main()