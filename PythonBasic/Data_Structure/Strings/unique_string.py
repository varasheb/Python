# 7. Write a Python program that accepts a comma separated sequence of words as input
# and prints the unique words in sorted form (alphanumerically).
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red

def unique_sorted_words(input_string):
    words = input_string.split(',')
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    
    for i in range(len(unique_words)):
        for j in range(len(unique_words) - 1):
            if unique_words[j] > unique_words[j + 1]:
                unique_words[j], unique_words[j + 1] = unique_words[j + 1], unique_words[j]

    return unique_words

def main():
    input_string = "red,white,black,red,green,black"
    print("Unique sorted words:", unique_sorted_words(input_string))
main()