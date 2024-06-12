# 2. Write a Python program to reverse the order of the items in the array.

import array

def reverse_array(arr):
    n = len(arr)
    for i in range(n // 2):
        temp = arr[i]
        arr[i] = arr[n - 1 - i]
        arr[n - 1 - i] = temp
def main():
     arr = array.array('i', [1, 2, 3, 4, 5])
     
     reverse_array(arr)
     
     print("Reversed array:", arr)

main()