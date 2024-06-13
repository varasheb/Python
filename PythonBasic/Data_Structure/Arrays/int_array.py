# 1. Write a Python program to create an array of 5 integers and display the array items.
# Access individual element through indexes.
import array

def main():
    arr = array.array('i', [1, 2, 3, 4, 5])
    print(type(arr))
    print("Array items:", arr)
    
    for i in range(len(arr)):
        print(f"Element at index {i}: {arr[i]}")
    
main()