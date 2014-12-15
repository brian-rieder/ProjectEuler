__author__ = 'Brian Rieder'

# Problem 7: 10001st Prime

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

# Answer: 104743

count = 6
prime_check = 15


def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**.5) + 1):
        if num % i == 0:
            return False
    return True

while count != 10001:
    prime_check += 2
    if is_prime(prime_check):
        count += 1

print(prime_check)