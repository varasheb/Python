# 8. Write a Python program to get the last part of a string before a specified character.


def last_part_before_char(s, char):
    index = -1
    for i in range(len(s)):
        if s[i] == char:
            index = i
            break
    if index != -1:
        return s[:index]
    return s

def main():
    input_string = "https://www.w3resource.com/python-exercises"
    specified_char = '/'
    print("Last part before character:", last_part_before_char(input_string, specified_char))
    
main()