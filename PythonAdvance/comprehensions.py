# Comprehensions in Python

# List Comprehensions

squares = [x * x for x in range(10)]
print(squares)  

# With Condition:

even_squares = [x * x for x in range(10) if x % 2 == 0]
print(even_squares) 

# Nested Loops:

combinations = [(x, y) for x in range(3) for y in range(3)]
print(combinations) 

# Dictionary Comprehensions

squares_dict = {x: x * x for x in range(10)}
print(squares_dict) 

# With Condition:

even_squares_dict = {x: x * x for x in range(10) if x % 2 == 0}
print(even_squares_dict)  

# Set Comprehensions

unique_squares = {x * x for x in range(-5, 6)}
print(unique_squares) 

# With Condition:

even_unique_squares = {x * x for x in range(-5, 6) if x % 2 == 0}
print(even_unique_squares)  

# Tuple Comprehensions 

gen_exp = (x * x for x in range(10))
print(tuple(gen_exp))  

# With Condition:

gen_exp = (x * x for x in range(10) if x % 2 == 0)
print(tuple(gen_exp))  

# Nested Comprehensions

matrix = [[j for j in range(5)] for i in range(5)]
print(matrix)
# Output:
# [
#   [0, 1, 2, 3, 4],
#   [0, 1, 2, 3, 4],
#   [0, 1, 2, 3, 4],
#   [0, 1, 2, 3, 4],
#   [0, 1, 2, 3, 4]
# ]


nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list) 