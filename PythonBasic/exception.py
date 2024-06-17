# Basic Exception Handling
# Using try-except Block
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero!")

try:
    number = int("not a number")
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Invalid number format!")


# Generic except Block
try:
    result = 10 / 0
except Exception as e:
    print(f"An error occurred: {e}")


# Using else Block
try:
    result = 10 / 2
except ZeroDivisionError:
    print("You cannot divide by zero!")
else:
    print("The result is:", result)


# Using finally Block
try:
    result = 10 / 2
except ZeroDivisionError:
    print("You cannot divide by zero!")
else:
    print("The result is:", result)
finally:
    print("This block always executes.")


# Raising Exceptions
def check_positive(number):
    if number < 0:
        raise ValueError("The number is negative!")

try:
    check_positive(-1)
except ValueError as e:
    print(e)

# Custom Exceptions
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error!")
except CustomError as e:
    print(e)


