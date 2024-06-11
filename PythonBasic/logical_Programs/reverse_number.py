# 4. Reverse a number
# we can reverse a number either by using for loop, while loop, or using recursion.
# The simplest way to reverse a number is by using for loop or while loop. In order to
# reverse a number, we have to follow the following steps:
# a. We need to calculate the remainder of the number using the modulo
# b. After that, we need to multiply the variable reverse by 10 and add the remainder into
# it.
# c. We then divide the number by 10 and repeat steps until the number becomes 0

def reverse_number(num):
    reversed_num = 0
    while num > 0:
        remainder = num % 10
        reversed_num = reversed_num * 10 + remainder
        num = num // 10
    return reversed_num

def main():
    num = int(input("Enter a number to reverse: "))
    reversed_num = reverse_number(num)
    print("Reversed number:", reversed_num)


main()
