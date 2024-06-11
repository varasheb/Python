# 2. Perfect Number
# a. Just like the Armstrong number, the Perfect Number is also a special type of
# positive number. When the number is equal to the sum of its positive divisors
# excluding the number, it is called a Perfect Number. For example, 28 is the perfect
# number because when we sum the divisors of 28, it will result in the same number.
# The divisors of 28 are 1, 2, 4, 7, and 14. So,
# b. 28 = 1+2+4+7
# c. 28 = 28

def is_perfect_number(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
         sum+=i
    return sum==num

def main():
    num=input('Enter the a Number :')
     
    if is_perfect_number(int(num)):
       print(f'{num} is Perfect Number')
    else:
       print('Not a Perfect Number!!!!!')
main()