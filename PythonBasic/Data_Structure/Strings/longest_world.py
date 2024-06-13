# 5. Write a Python function that takes a list of words and returns the length of the longest one.

def longest_word_length(words):
    max_length = 0
    for word in words:
        length = len(word)
        if length > max_length:
            max_length = length
    return max_length

def main():
    words_list = ["hello", "world", "python", "programming"]
    print("Length of the longest word:", longest_word_length(words_list))
main()