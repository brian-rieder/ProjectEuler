__author__ = 'Brian Rieder'

# Problem 5: Smallest Multiple


# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Answer: 232792560


check = False
i = 2520
while not check:
    i += 2520
    check_div = True
    for j in range(11, 20):
        if i % j != 0:
            check_div = False
            break
    if check_div:
        check = True
print(i)