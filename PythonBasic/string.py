a = "Hello, World!"
print(a[1])
print(type(a[1]))

print('this timy cook the ceo of apple coportation %s'%(a))

print(len(a))

txt = "The best things in life are free!"
print("free" in txt)
print("expensive" not in txt)

# Slicing

b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])

c='varshab'
print(c.upper())
c="HILLRAY CLINTON"
print(c.lower())

a = " Hello, World! this is me ,the greatest programer   "
print(a.strip())
print(a.replace(" me ", " Varshab "))
print(a.split(","))

# F-Strings
# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59.56
txt = f"The price is {price:.2f} dollars"
print(txt)


# capitalize() - Converts the first character to upper case
print("hello world".capitalize())  # Output: "Hello world"

# casefold() - Converts string into lower case
print("HELLO WORLD".casefold())  # Output: "hello world"

# center() - Returns a centered string
print("hello".center(20, '-'))  # Output: "-------hello--------"

# count() - Returns the number of times a specified value occurs in a string
print("hello world".count('o'))  # Output: 2

# encode() - Returns an encoded version of the string
print("hello".encode())  # Output: b'hello'

# endswith() - Returns true if the string ends with the specified value
print("hello world".endswith("world"))  # Output: True

# expandtabs() - Sets the tab size of the string
print("hello\tworld".expandtabs(4))  # Output: "hello   world"

# find() - Searches the string for a specified value and returns the position of where it was found
print("hello world".find('world'))  # Output: 6

# format() - Formats specified values in a string
print("Hello, {}!".format("world"))  # Output: "Hello, world!"

# format_map() - Formats specified values in a string
print("Hello, {name}!".format_map({"name": "world"}))  # Output: "Hello, world!"

# index() - Searches the string for a specified value and returns the position of where it was found
print("hello world".index('world'))  # Output: 6

# isalnum() - Returns True if all characters in the string are alphanumeric
print("hello123".isalnum())  # Output: True

# isalpha() - Returns True if all characters in the string are in the alphabet
print("hello".isalpha())  # Output: True

# isascii() - Returns True if all characters in the string are ascii characters
print("hello".isascii())  # Output: True

# isdecimal() - Returns True if all characters in the string are decimals
print("123".isdecimal())  # Output: True

# isdigit() - Returns True if all characters in the string are digits
print("123".isdigit())  # Output: True

# isidentifier() - Returns True if the string is an identifier
print("hello".isidentifier())  # Output: True

# islower() - Returns True if all characters in the string are lower case
print("hello".islower())  # Output: True

# isnumeric() - Returns True if all characters in the string are numeric
print("123".isnumeric())  # Output: True

# isprintable() - Returns True if all characters in the string are printable
print("hello".isprintable())  # Output: True

# isspace() - Returns True if all characters in the string are whitespaces
print("   ".isspace())  # Output: True

# istitle() - Returns True if the string follows the rules of a title
print("Hello World".istitle())  # Output: True

# isupper() - Returns True if all characters in the string are upper case
print("HELLO".isupper())  # Output: True

# join() - Joins the elements of an iterable to the end of the string
print(", ".join(["hello", "world"]))  # Output: "hello, world"

# ljust() - Returns a left justified version of the string
print("hello".ljust(10, '-'))  # Output: "hello-----"

# lower() - Converts a string into lower case
print("HELLO".lower())  # Output: "hello"

# lstrip() - Returns a left trim version of the string
print("   hello".lstrip())  # Output: "hello"

# maketrans() - Returns a translation table to be used in translations
trans = str.maketrans("aeiou", "12345")
print("hello".translate(trans))  # Output: "h2ll4"

# partition() - Returns a tuple where the string is parted into three parts
print("hello world".partition(" "))  # Output: ('hello', ' ', 'world')

# replace() - Returns a string where a specified value is replaced with a specified value
print("hello world".replace("world", "Python"))  # Output: "hello Python"

# rfind() - Searches the string for a specified value and returns the last position of where it was found
print("hello world".rfind('o'))  # Output: 7

# rindex() - Searches the string for a specified value and returns the last position of where it was found
print("hello world".rindex('o'))  # Output: 7

# rjust() - Returns a right justified version of the string
print("hello".rjust(10, '-'))  # Output: "-----hello"

# rpartition() - Returns a tuple where the string is parted into three parts
print("hello world".rpartition(" "))  # Output: ('hello', ' ', 'world')

# rsplit() - Splits the string at the specified separator, and returns a list
print("hello world".rsplit(" "))  # Output: ['hello', 'world']

# rstrip() - Returns a right trim version of the string
print("hello   ".rstrip())  # Output: "hello"

# split() - Splits the string at the specified separator, and returns a list
print("hello world".split(" "))  # Output: ['hello', 'world']

# splitlines() - Splits the string at line breaks and returns a list
print("hello\nworld".splitlines())  # Output: ['hello', 'world']

# startswith() - Returns true if the string starts with the specified value
print("hello world".startswith("hello"))  # Output: True

# strip() - Returns a trimmed version of the string
print("   hello   ".strip())  # Output: "hello"

# swapcase() - Swaps cases, lower case becomes upper case and vice versa
print("Hello World".swapcase())  # Output: "hELLO wORLD"

# title() - Converts the first character of each word to upper case
print("hello world".title())  # Output: "Hello World"

# translate() - Returns a translated string
trans = str.maketrans("aeiou", "12345")
print("hello".translate(trans))  # Output: "h2ll4"

# upper() - Converts a string into upper case
print("hello".upper())  # Output: "HELLO"

# zfill() - Fills the string with a specified number of 0 values at the beginning
print("42".zfill(5))  # Output: "00042"
