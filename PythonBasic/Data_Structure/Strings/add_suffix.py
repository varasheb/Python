# 4. Write a Python program to add 'ing' at the end of a given string (length should be at
# least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the
# given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

def add_suffix(s):
    length = len(s)
    if length >= 3:
        if s[-3:] == "ing":
            return s + "ly"
        else:
            return s + "ing"
    else:
        return s

def main():
    input_string = "abc"
    print("Modified string:", add_suffix(input_string))
    input_string = "string"
    print("Modified string:", add_suffix(input_string))
    
main()