# 12. Write a Python program to find maximum and the minimum value in a set.

def max_min_value(my_set):
    max_value = float('-inf')
    min_value = float('inf')
    for item in my_set:
        if item > max_value:
            max_value = item
        if item < min_value:
            min_value = item
    print("Maximum value:", max_value)
    print("Minimum value:", min_value)

def main():
        my_set = {3, 5, 2, 8, 1}
        max_min_value(my_set)
        
main()
