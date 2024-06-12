# 3. Write a Python program to get the number of occurrences of a specified element in an array

import array

def get_occurance_of_element(element,arr):
    occurrences = 0
    for item in arr:
     if item == element:
          occurrences += 1
    return occurrences

def main():
   arr = array.array('i', [1, 2, 3, 2, 5, 2, 3])
   element = 2
   print(f"Number of occurrences of {element}: {get_occurance_of_element(element,arr)}")

main()
