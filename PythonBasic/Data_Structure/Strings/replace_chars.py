# 3. Write a Python program to get a string from a given string where all occurrences of its
# first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

def replace_chars(s):
    if len(s) == 0:
        return s
    first_char = s[0]
    result = first_char
    for char in s[1:]:
        if char == first_char:
            result += '$'
        else:
            result += char
    return result

def main():
    input_string = "restart"
    print("Modified string:", replace_chars(input_string))

main()