# 7. Write a Python program to create a union of sets.

def union(set1, set2):
    union_set = set()
    for item in set1:
        union_set.add(item)
    for item in set2:
        union_set.add(item)
    return union_set

def main():
    set1 = {1, 2, 3 , 4}
    set2 = {3, 4, 5 , 6}
    
    print("Union of sets:", union(set1, set2))

main()