str="hello niha bonjor Kon'nichiwa privet Hola"
# print(str.count('e'))
# # print(str.rsplit([0-9]))
# str_list=[i for i in str]
# str_list.sort()

def looper(str):
    loopitertator=str.__iter__()
    def looping():
            try:
                print(loopitertator.__next__())
                looping()
            except StopIteration:
                 exit
    looping()
                  


looper(str)
#+++++++++++++++++++++++++++++++++++++++++++
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squares = map(square, numbers)

# Convert map object to a list
squares_list = list(squares)
print(squares_list)

#====================================

numbers = [10, 20, 30, 40, 50]
squares = map(lambda x: x ** 2, numbers)
squares_list = list(squares)
print("Squares with lambda:", squares_list)


def add(x, y):
    return x + y

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(add, numbers1, numbers2)
result_list = list(result)
print("Addition of two lists:", result_list)


numbers = [1, 2, 3, 4, 5]
squares = map(lambda x: x ** 2, numbers)


squares_tuple = tuple(squares)
print("Squares tuple:", squares_tuple)


numbers1 = [1, 2, 3]
numbers2 = [4, 5]
result = map(lambda x, y: x + y, numbers1, numbers2)
result_list = list(result)
print("Addition with different lengths:", result_list)


def capitalize_string(s):
    return s.capitalize()

strings = ['hello', 'world']
capitalized_strings = map(capitalize_string, strings)
capitalized_list = list(capitalized_strings)
print("Capitalized strings:", capitalized_list)

#=================================
numbers = [1, 2, 3, 4, 5]
squares = map(lambda x: x ** 2, numbers)
squares_set = set(squares)
print("Squares set:", squares_set)

#================================
strings = ["123", "456", "789"]
integers = map(int, strings)
integers_list = list(integers)
print("Converted to integers:", integers_list)

#================================
def multiply(x, y):
    return x * y

numbers1 = [1, 2, 3, 4]
numbers2 = [10, 20, 30]
result = map(multiply, numbers1, numbers2)
result_list = list(result)
print("Multiplication of two lists:", result_list)


