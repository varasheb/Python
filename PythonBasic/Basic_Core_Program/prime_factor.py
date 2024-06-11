
# 5. Factors
# a. Desc -> Computes the prime factorization of N using brute force.
# b. I/P -> Number to find the prime factors
# c. Logic -> Traverse till i*i <= N instead of i <= N for efficiency.
# d. O/P -> Print the prime factors of number N.

def prime_factors(n):
    i=2
    while i*i<=n:
        if n%i==0:
            print(i)
            n//=i
        else:
            i+=1
    if n>i:
        print(n)
def main():
        n = int(input("Enter a number to find its prime factors: "))
        print("Prime factors of", n, "are:")
        prime_factors(n)

main()