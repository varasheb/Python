# 8. Write a Python program to find the list of words that are longer than n from a
# given list of words.

def longer_than_n(words, n):
    result = []
    for word in words:
        if len(word) > n:
            result.append(word)
    return result

def main():
    words = ['apple', 'banana', 'kiwi', 'orange']
    n = 4
    print("Words longer than", n, "characters:", longer_than_n(words, n))

main()
