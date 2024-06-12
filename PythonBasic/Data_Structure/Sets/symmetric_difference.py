# 9. Write a Python program to create a symmetric difference.

def symmetric_difference(set1, set2):
    symm_diff_set = set()
    for item in set1:
        if item not in set2:
            symm_diff_set.add(item)
    for item in set2:
        if item not in set1:
            symm_diff_set.add(item)
    return symm_diff_set

def main():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    
    print("Symmetric difference:", symmetric_difference(set1, set2))

main()