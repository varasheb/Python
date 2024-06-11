# 1. Flip Coin and print percentage of Heads and Tails
# a. I/P -> The number of times to Flip Coin. Ensure it is a positive integer.
# b. Logic -> Use Random Function to get value between 0 and 1. If < 0.5 then tails or
# heads
# c. O/P -> Percentage of Head vs Tails
import random

def flip_coin():
    return random.randint(0,1)

def calculate_head_tail_percentage(total_flip):
    if total_flip <= 0:
        return "Total flips should be a positive integer"
    i=total_flip
    head_count=0
    tail_count=0
    while(i>0):
        if(flip_coin()==0):
            head_count+=1
        else:
            tail_count+=1

        i-=1
    return {'head' :head_count/total_flip*100,'tail' :tail_count/total_flip*100}  


print(calculate_head_tail_percentage(10))
