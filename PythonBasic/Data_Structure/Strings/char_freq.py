# 2. Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

def char_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def main():
    input_string = "google.com"
    print("Character frequency:", char_frequency(input_string))

main()