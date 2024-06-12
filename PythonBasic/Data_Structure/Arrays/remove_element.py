# 4. Write a Python program to remove the first occurrence of a specified element from an array.

import array


def remove_first_occurrence(arr, element_to_remove):
    index_to_remove = -1
    for i in range(len(arr)):
        if arr[i] == element_to_remove:
            index_to_remove = i
            break
    
    if index_to_remove != -1:
        for i in range(index_to_remove, len(arr) - 1):
            arr[i] = arr[i + 1]
        arr.pop()


def main():
    arr = array.array('i', [1, 2, 3, 2, 5])
    element_to_remove = 2
    remove_first_occurrence(arr, element_to_remove)
    print("Array after removing the first occurrence of", element_to_remove, ":",arr)

main()


