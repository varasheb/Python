# 3. Prime Number
# Just like the Perfect number, the Prime number is also a special type of number. When
# the number is divided greater than 1 and divided by 1 or itself is referred to as the Prime
# number. 0 and 1 are not counted as prime numbers. All the even numbers can be
# divided by 2, so 2 is the only even prime minister


def is_prime_number(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
        
    return True

def main():
    num=input('Enter the a Number :')
     
    if is_prime_number(int(num)):
       print(f'{num} is Prime Number')
    else:
       print('Not a Prime Number!!!!')
main()