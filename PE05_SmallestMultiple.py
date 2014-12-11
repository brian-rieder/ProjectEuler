__author__ = 'Brian Rieder'

# Problem 5: Smallest Multiple


# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Answer: 232792560

num = 20
while True:
    if num % 2 == 0:
        if num % 3 == 0:
            if num % 5 == 0:
                if num % 7 == 0:
                    print num
                    if num % 11 == 0:
                        if num % 13 == 0:
                            if num % 17 == 0:
                                if num % 19 == 0:
                                    print num
                                    break
    num += 20