# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math

def isPrime(num):
    if(num % 2 == 0):
        return 0
    root = math.floor(math.sqrt(num))
    i = 3
    while i < root:
        if(num % i == 0):
            return 0
        i += 1
    return 1

def calcBigPrime():
    bignum = 58
    numroot = math.floor(math.sqrt(bignum))
    largestprime = 2
    i = 3
    while(i < numroot):
        if(isPrime(i)):
            largestprime = i;
            print("Largest Prime: ", largestprime)
        i += 2

calcBigPrime()

