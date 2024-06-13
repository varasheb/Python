# 1. Write a Python program to calculate the length of a string.


def string_length(s):
    length = 0
    for char in s:
        length += 1
    return length

def main():
    input_string = "hello"
    print("Length of the string:", string_length(input_string))
    
main()