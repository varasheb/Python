# 10. Write a Python program to print a specified list after removing the 0th, 4th and
# 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

def remove_elements(items, indices):
    result = []
    for i in range(len(items)):
        if i not in indices:
            result.append(items[i])
    return result

def main():
    items = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    indices = [0, 4, 5]
    print("List after removing 0th, 4th, and 5th elements:", remove_elements(items, indices))


main()
