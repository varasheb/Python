def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(is_even, numbers)
even_numbers_list = list(even_numbers)
print("Even numbers:", even_numbers_list)

numbers = [1, 2, 3, 4, 5, 6]
odd_numbers = filter(lambda x: x % 2 != 0, numbers)
odd_numbers_list = list(odd_numbers)
print("Odd numbers with lambda:", odd_numbers_list)

def is_uppercase(s):
    return s.isupper()

strings = ['Hello', 'WORLD', 'PYTHON', 'code']
uppercase_strings = filter(is_uppercase, strings)
uppercase_list = list(uppercase_strings)
print("Uppercase strings:", uppercase_list)

def is_positive_and_even(x):
    return x > 0 and x % 2 == 0

numbers = [-10, -5, 0, 5, 10, 15, 20]
positive_even_numbers = filter(is_positive_and_even, numbers)
positive_even_list = list(positive_even_numbers)
print("Positive and even numbers:", positive_even_list)

mixed = [0, 1, '', 'Hello', None, True, False, [], [1, 2, 3]]
truthy_values = filter(None, mixed)
truthy_list = list(truthy_values)
print("Truthy values:", truthy_list)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [
    Person("Alice", 30),
    Person("Bob", 15),
    Person("Charlie", 25),
    Person("Diana", 20)
]

def is_adult(person):
    return person.age >= 18

adults = filter(is_adult, people)
adults_list = list(adults)
adult_names = [person.name for person in adults_list]
print("Adults:", adult_names)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = filter(lambda x: all(x % i != 0 for i in range(2, x)), numbers)
prime_list = list(prime_numbers)
print("Prime numbers:", prime_list)


students = [
    {"name": "varshab", "grade": 85},
    {"name": "preteek", "grade": 75},
    {"name": "ramesh", "grade": 95},
    {"name": "Diana", "grade": 60}
]

def has_passed(student):
    return student["grade"] >= 70

passed_students = filter(has_passed, students)
passed_students_list = list(passed_students)
passed_names = [student["name"] for student in passed_students_list]
print("Passed students:", passed_names)

data = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
filtered_data = filter(lambda x: x[0] % 2 == 0, data)
filtered_data_list = list(filtered_data)
print("Filtered tuples:", filtered_data_list)

def is_vowel(char):
    return char.lower() in 'aeiou'

characters = 'The quick brown fox jumps over the lazy dog'
vowels = filter(is_vowel, characters)
vowels_list = list(vowels)
print("Vowels in string:", vowels_list)
