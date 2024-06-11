# 5. Coupon Numbers
# a. Desc -> Given N distinct Coupon Numbers, how many random numbers do you
# need to generate a distinct coupon number? This program simulates this random
# process.
# b. I/P -> N Distinct Coupon Number
# c. Logic -> repeatedly choose a random number and check whether it's a new one.
# d. O/P -> total random number needed to have all distinct numbers.
# e. Functions => Write Class Static Functions to generate random numbers and to
# process distinct coupons

import random

def generate_distinct_coupons(N):
    coupons = set()
    random_numbers = 0
    while len(coupons) < N:
        coupon = random.randint(1, N)
        coupons.add(coupon)
        random_numbers += 1
    return random_numbers

def main():
    N = int(input("Enter the number of distinct coupon numbers: "))
    random_numbers = generate_distinct_coupons(N)
    print("Total random numbers needed to have all distinct numbers:", random_numbers)


main()
