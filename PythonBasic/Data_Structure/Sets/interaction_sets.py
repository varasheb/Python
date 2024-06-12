# 6. Write a Python program to create an intersection of sets.


def intersection(set1, set2):
    intersection_set = set()
    for item in set1:
        if item in set2:
            intersection_set.add(item)
    return intersection_set

def main():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    print("Intersection of sets:", intersection(set1, set2))

main()