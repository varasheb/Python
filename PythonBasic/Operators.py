# 1. Arithmetic Operators

a = 10
b = 3

print("Addition:", a + b)        # 13
print("Subtraction:", a - b)     # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)        # 3.3333...
print("Modulus:", a % b)         # 1
print("Exponentiation:", a ** b) # 1000
print("Floor Division:", a // b) # 3

# 2. Assignment Operators

x = 5          # x = 5
x += 3         # x = x + 3 => x = 8
x -= 2         # x = x - 2 => x = 6
x *= 4         # x = x * 4 => x = 24
x /= 6         # x = x / 6 => x = 4.0
x %= 3         # x = x % 3 => x = 1.0
x **= 2        # x = x ** 2 => x = 1.0
x //= 1        # x = x // 1 => x = 1.0

# 3. Comparison Operators

a = 10
b = 20

print("Equal:", a == b)            # False
print("Not Equal:", a != b)        # True
print("Greater Than:", a > b)      # False
print("Less Than:", a < b)         # True
print("Greater or Equal:", a >= b) # False
print("Less or Equal:", a <= b)    # True

# 4. Logical Operators

a = True
b = False

print("AND:", a and b)  # False
print("OR:", a or b)    # True
print("NOT:", not a)    # False

# 5. Identity Operators

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("Is:", a is b)       # False (different objects in memory)
print("Is Not:", a is not b) # True
print("Is:", a is c)       # True (same object in memory)

# 6. Membership Operators

a = [1, 2, 3, 4, 5]

print("In:", 3 in a)         # True
print("Not In:", 6 not in a) # True

# 7. Bitwise Operators

a = 10     # 1010 in binary
b = 4      # 0100 in binary

print("AND:", a & b)  # 0000 => 0
print("OR:", a | b)   # 1110 => 14
print("XOR:", a ^ b)  # 1110 => 14
print("NOT:", ~a)     # -1011 => -11 formula -(x+1)
print("Left Shift:", a << 1)  # 10100 => 20
print("Right Shift:", a >> 1) # 0101 => 5