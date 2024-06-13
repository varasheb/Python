# 6. Write a Python script that takes input from the user and displays that input back in
# upper and lower cases.
# 10. Write a Python program to count occurrences of a substring in a string.
# 11. Write a Python program to reverse a string.
# 12. Write a Python program to lowercase first n characters in a string.



def to_upper_case(s):
    upper_case = ""
    for char in s:
        if 'a' <= char <= 'z':
            upper_case += chr(ord(char) - 32)
        else:
            upper_case += char
    return upper_case

def to_lower_case(s):
    lower_case = ""
    for char in s:
        if 'A' <= char <= 'Z':
            lower_case += chr(ord(char) + 32)
        else:
            lower_case += char
    return lower_case


def count_substring_occurrences(s, sub):
    count = 0
    for i in range(len(s) - len(sub) + 1):
        if s[i:i + len(sub)] == sub:
            count += 1
    return count


def reverse_string(s):
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str


def lowercase_first_n(s, n):
    lowercased = ""
    for i in range(len(s)):
        if i < n and 'A' <= s[i] <= 'Z':
            lowercased += chr(ord(s[i]) + 32)
        else:
            lowercased += s[i]
    return lowercased



def main():
    # 6
    user_input = input("Enter a string: ")
    print("Upper case:", to_upper_case(user_input))
    print("Lower case:", to_lower_case(user_input))
    
    # 10
    input_string = "hello world, hello universe"
    substring = "hello"
    print("Occurrences of substring:", count_substring_occurrences(input_string, substring))
    
    
    # 11
    input_string = "hello"
    print("Reversed string:", reverse_string(input_string))
    
    # 12
    n = 2
    print("Lowercased first n characters:", lowercase_first_n(user_input, n))
    
main()