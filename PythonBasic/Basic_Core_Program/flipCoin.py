# 1. Flip Coin and print percentage of Heads and Tails
# a. I/P -> The number of times to Flip Coin. Ensure it is a positive integer.
# b. Logic -> Use Random Function to get value between 0 and 1. If < 0.5 then tails or
# heads
# c. O/P -> Percentage of Head vs Tails
import random

def flipcoin():
    return random.randint(0,1)

def calculateHeadTailPercentage(totalflip):
    if totalflip <= 0:
        return "Total flips should be a positive integer"
    i=totalflip
    headCount=0
    tailCount=0
    while(i>0):
        if(flipcoin()==0):
            headCount+=1
        else:
            tailCount+=1

        i-=1
    return {'head' :headCount/totalflip*100,'tail' :tailCount/totalflip*100}  


print(calculateHeadTailPercentage(10))
