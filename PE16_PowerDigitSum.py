__author__ = 'Brian Rieder'

# Problem 16: Power Digit Sum

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?

# Answer: 1366

check = 1000


def sum_digits(num):
    list_pow = list(str(2**num))
    sum_val = sum(int(i) for i in list_pow)
    return sum_val

print(sum_digits(check))