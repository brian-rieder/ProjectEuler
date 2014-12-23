__author__ = 'Brian Rieder'

# Problem 23: Non-abundant Sums

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
# the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if
# this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum
# of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can
# be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis
# even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less
# than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


def sum_proper_divisors(num):
    test_val = 1
    sum_val = 0
    while test_val <= (num/2):
        if num % test_val == 0:
            sum_val += test_val
        test_val += 1
    return sum_val


def is_abundant(num):
    check = sum_proper_divisors(num)
    if check > num:
        return True
    else:
        return False


def is_summable_by_abundant(num):
    for j in range(12, int(num/2) + 1):
        if is_abundant(j):
            if is_abundant(num - j):
                return True
    return False


# final_sum = 0
# for i in range(24, 28124):
#     if is_summable_by_abundant(i):
#         final_sum += i
#
# print("Final sum:" + final_sum)


abundant = []
for i in range(12, 28125):
    if is_abundant(i):
        abundant.append(i)

hash_list = [False] * 28125
for i in hash_list:
    for k in hash_list:
        if abundant[i] + abundant[k] <= 28124:
            hash_list[abundant[i] + abundant[k]] = True

final_sum = 0
for i in hash_list:
    if not hash_list:
        final_sum += i