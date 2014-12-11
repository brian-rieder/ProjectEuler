__author__ = 'Brian Rieder'

# Problem 2: Even Fibonacci Numbers

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2,
# the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the
# even-valued terms.

# Answer: 4613732


def fibonacci(val):
    if val == 0:
        return 1
    elif val == 1:
        return 1
    return fibonacci(val-1) + fibonacci(val-2)


fib_val = 0
itr = 0
sum_val = 0
while fib_val < 4000000:
    fib_val = fibonacci(itr)
    if fib_val % 2 == 0:
        sum_val += fib_val
    itr += 1


print sum_val