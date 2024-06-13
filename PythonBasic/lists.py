# append(): Adds an element at the end of the list.
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # Output: [1, 2, 3, 4]

# clear(): Removes all the elements from the list.
numbers = [1, 2, 3]
numbers.clear()
print(numbers)  # Output: []

# copy(): Returns a copy of the list.
numbers = [1, 2, 3]
numbers_copy = numbers.copy()
print(numbers_copy)  # Output: [1, 2, 3]

# count(): Returns the number of elements with the specified value.
numbers = [1, 2, 2, 3, 2]
count = numbers.count(2)
print(count)  # Output: 3

# extend(): Add the elements of a list (or any iterable), to the end of the current list.
numbers = [1, 2, 3]
numbers.extend([4, 5])
print(numbers)  # Output: [1, 2, 3, 4, 5]

# index(): Returns the index of the first element with the specified value.
numbers = [1, 2, 3, 4, 5]
index = numbers.index(3)
print(index)  # Output: 2

# insert(): Adds an element at the specified position.
numbers = [1, 2, 3]
numbers.insert(1, 1.5)
print(numbers)  # Output: [1, 1.5, 2, 3]


# pop(): Removes the element at the specified position and returns it.
numbers = [1, 2, 3]
popped_element = numbers.pop(1)
print(popped_element)  # Output: 2
print(numbers)         # Output: [1, 3]

# remove(): Removes the item with the specified value.
numbers = [1, 2, 3, 4, 5]
numbers.remove(3)
print(numbers)  # Output: [1, 2, 4, 5]


# reverse(): Reverses the order of the list.
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # Output: [5, 4, 3, 2, 1]

# sort(): Sorts the list.
numbers = [3, 1, 2, 5, 4]
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 4, 5]