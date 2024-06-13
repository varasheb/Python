# 1. Write a Python program to create a tuple.
# 2. Write a Python program to create a tuple with different data types.
# 3. Write a Python program to unpack a tuple in several variables.
# 4. Write a Python program to create the colon of a tuple.
# 6. Write a Python program to check whether an element exists within a tuple.
# 7. Write a Python program to convert a list to a tuple.




def check_element_existence(element,my_tuple):    
    if element in my_tuple:
        print("Element", element, "exists in the tuple")
    else:
        print("Element", element, "does not exist in the tuple")


def main():
    #1
    my_tuple = (1, 2, 3, 4, 5)
    print("Tuple:", my_tuple)

    #2
    mixed_tuple = (1, "hello", 3.14, True)
    print("Mixed tuple:", mixed_tuple)

    #3 Unpack a tuple into several variables
    my_tuple = (1, 2, 3)
    a, b, c = my_tuple
    print("Unpacked variables:", a, b, c)
    
    #4: Create a colon of a tuple
    my_tuple = (1, 2, 3, 4, 5)
    colon_tuple = my_tuple + (':',)
    print("Colon tuple:", colon_tuple)
    
    #6: Check if an element exists within a tuple
    my_tuple = (1, 2, 3, 4, 5)
    element = 3
    check_element_existence(element,my_tuple)

    # 7: Convert a list to a tuple
    my_list = [1, 2, 3, 4, 5]
    converted_tuple = tuple(my_list)
    print("Converted tuple:", converted_tuple)


main()
