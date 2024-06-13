# 1. Write a Python program to create a set.
# 2. Write a Python program to iteration over sets.
# 3. Write a Python program to add member(s) in a set.
# 10. Write a Python program to clear a set.
 
def clear_set(my_set):
    my_set = set()
    print("Set after clearing:", my_set)

def main():
    # Task 1: Create a set
    my_set = {1, 2, 3, 4, 5}
    print("Set:", my_set)

    # Task 2: Iterate over a set
    my_set = {1, 2, 3, 4, 5}
    print("Set elements:")
    for item in my_set:
        print(item)

    # Task 3: Add members to a set
    my_set = {1, 2, 3}
    my_set.add(4)
    my_set.update([5, 6, 7])
    print("Set after adding members:", my_set)   


    # Task 10: Clear a set
    my_set = {1, 2, 3, 4, 5}
    clear_set(my_set)


main()
