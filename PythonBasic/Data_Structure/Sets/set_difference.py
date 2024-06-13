# 8. Write a Python program to create set difference.

def set_difference(set1, set2):
    diff_set = set()
    for item in set1:
        if item not in set2:
            diff_set.add(item)
    return diff_set

def main():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    
    print("Set difference:", set_difference(set1, set2))

main()