__author__ = 'Brian Rieder'

# Problem 1: Multiples of 3

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of
# these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Answer: 233168


def gen_sum_multiples5(num):
    sum_val = 0
    mult_val = 0
    while mult_val < num:
        if mult_val % 3 != 0:
            sum_val += mult_val
        mult_val += 5
    return sum_val


def gen_sum_multiples3(num):
    sum_val = 0
    mult_val = 0
    while mult_val < num:
        sum_val += mult_val
        mult_val += 3
    return sum_val


testval = 1000
print("Sum of all tested values for " + str(testval) + " are: " + str(gen_sum_multiples3(testval) +
                                                                      gen_sum_multiples5(testval)))