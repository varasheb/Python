a=[1,2,3,4,5,6,7]
print(type(a))
print(type(a[1]))



# 1. append() Adds an element at the end of the list.

fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# 2. clear() Removes all the elements from the list.

fruits = ['apple', 'banana', 'cherry']
fruits.clear()
print(fruits)  # Output: []


# 3. copy() Returns a copy of the list.

fruits = ['apple', 'banana', 'cherry']
fruits_copy = fruits.copy()
print(fruits_copy)  # Output: ['apple', 'banana', 'cherry']


# 4. count() Returns the number of elements with the specified value.

fruits = ['apple', 'banana', 'cherry', 'banana']
banana_count = fruits.count('banana')
print(banana_count)  # Output: 2

# 5. extend() Add the elements of a list (or any iterable) to the end of the current list.

fruits = ['apple', 'banana', 'cherry']
more_fruits = ['orange', 'mango', 'grapes']
fruits.extend(more_fruits)
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange', 'mango', 'grapes']

# 6. index() Returns the index of the first element with the specified value.

fruits = ['apple', 'banana', 'cherry']
banana_index = fruits.index('banana')
print(banana_index)  # Output: 1

# 7. insert() Adds an element at the specified position.

fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, 'orange')
print(fruits)  # Output: ['apple', 'orange', 'banana', 'cherry']

# 8. pop() Removes the element at the specified position.

fruits = ['apple', 'banana', 'cherry']
popped_fruit = fruits.pop(1)
print(fruits)  # Output: ['apple', 'cherry']
print(popped_fruit)  # Output: 'banana'

# 9. remove() Removes the first item with the specified value.

fruits = ['apple', 'banana', 'cherry', 'banana']
fruits.remove('banana')
print(fruits)  # Output: ['apple', 'cherry', 'banana']

# 10. reverse() Reverses the order of the list.

fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)  # Output: ['cherry', 'banana', 'apple']

# 11. sort() Sorts the list.

fruits = ['banana', 'apple', 'cherry']
fruits.sort()
print(fruits)  # Output: ['apple', 'banana', 'cherry']