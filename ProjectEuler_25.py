__author__ = 'Brian Rieder'

# Problem 25: 1000-digit Fibonacci Number

# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
#
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
#
# What is the first term in the Fibonacci sequence to contain 1000 digits?

digit_check = 1000

def num_digits(number):
    return len(str(number))


def fibonacci():
    num1 = 1
    num2 = 1
    flag = 0
    cnter = 2
    while 1:
        if num_digits(num1) == digit_check:
            print(num1)
            return cnter
        elif num_digits(num2) == digit_check:
            print(num2)
            return cnter
        if flag:
            flag = 0
            num2 += num1
        elif ~flag:
            flag = 1
            num1 += num2
        cnter += 1


retval = fibonacci()
print('Value = ' + str(retval))