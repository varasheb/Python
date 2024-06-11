# 1. Fibonacci Series
# Fibonacci series is a special type of series in which the next term is the sum of the
# previous two terms. For example, if 0 and 1 are the two previous terms in a series, then
# the next term will be 1(0+1).


def fibonacci_series(n):
    next=1
    previous=0
    count=0
    while count<n:
        print(next,end=' ')
        temp=next
        next+=previous
        previous=temp
        count+=1
def main():
    n=input('Enter the value of N : ')
    fibonacci_series(int(n))
main()