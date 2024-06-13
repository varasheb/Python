# 1. Write a Python program to sum all the items in a list.

# 2. Write a Python program to multiplies all the items in a list.

# 3. Write a Python program to get the smallest number from a list.

# 7. Write a Python program to clone or copy a list.

# 13. Write a Python program to append a list to the second list.


def sum_list(items):
    total = 0
    for item in items:
        total += item
    return total

def multiply_list(items):
    result = 1
    for item in items:
        result *= item
    return result

def smallest_number(items):
    smallest = items[0]
    for item in items[1:]:
        if item < smallest:
            smallest = item
    return smallest

def clone_list(items):
    cloned = []
    for item in items:
        cloned.append(item)
    return cloned

def append_lists(left_list, right_list):
    for item in right_list:
        left_list.append(item)

def main():
    numbers = [1, 2, 3, 4, 5]
    print("Sum of all items:", sum_list(numbers))

    numbers = [1, 2, 3, 4, 5 ,7]
    print("Product of all items:", multiply_list(numbers))

    numbers = [5, 2, 7, 1, 9]
    print("Smallest number:", smallest_number(numbers))

    original = [1, 2, 3, 4, 5]
    cloned = clone_list(original)
    print("Cloned list:", cloned)

    left_list = [1, 2, 3]
    right_list = [4, 5, 6]
    append_lists(left_list, right_list)
    print("Appended list:", left_list)


main()
