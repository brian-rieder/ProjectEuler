__author__ = 'Brian Rieder'

# Problem 21: Amicable Numbers

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called
# amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.


def sum_proper_divisors(num):
    test_val = 1
    sum = 0
    while test_val <= (num/2):
        if num % test_val == 0:
            sum += test_val
        test_val += 1
    return sum


# This is wrong.... we want all amicable under 10000
def gen_10000_proper():
    a1 = []
    for i in range(0, 999):
        a1.append(sum_proper_divisors(i))
    return a1


# This isn't done.
def check_amicable(array):
    if 1:
        return array