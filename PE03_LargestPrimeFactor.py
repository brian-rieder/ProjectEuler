__author__ = 'Brian Rieder'

# Problem 3: Largest Prime Factor

# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

# Answer: 6857

from math import sqrt


def is_prime(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n % 2 == 0:
        return 0
    max_val = int(sqrt(n)) + 1
    for i in range(3, max_val, 2):
        if n % i == 0:
            return 0
    return 1


start_val = 600851475143
check_factor = int(sqrt(start_val)) + 1
while True:
    if (start_val % check_factor == 0) and (is_prime(check_factor)):
        break
    check_factor -= 1
print(check_factor)