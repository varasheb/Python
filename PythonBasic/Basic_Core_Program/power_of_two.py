"""
3. Power of 2
a. Desc -> This program takes a command-line argument N and prints a table of the
powers of 2 that are less than or equal to 2^N.
b. I/P -> The Power Value N. Only works if 0 <= N < 31 since 2^31 overflows an int
c. Logic -> repeat until i equals N.
"""
def print_power_of_two(n):
        if n>=0 and n<=31:
            print(f"Powers of 2 from 2^0 to 2^{n}:")
            for i in range(n+1):
                print(f"2^{i} = {2**i}")

        else:
            print('Invalid Input :  N must be in the range 0 <= N < 31')
     
def main():
    n=int(input('Enter the value of N :'))
    print_power_of_two(n)

main() 
