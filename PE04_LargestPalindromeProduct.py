__author__ = 'Brian Rieder'

# Problem 4: Largest Palindrome Product

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit
# numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

# Answer: 906609

def isPalindrome(seq1):
    seq2 = seq1[::-1]
    if(seq1 == seq2):
        return 1
    else:
        return 0

def genNumbers():
    largestpalin = 0
    for i in range(100,999):
        for j in range(100,999):
            prod = i * j
            if(isPalindrome(str(prod)) and prod > largestpalin):
                largestpalin = prod
    return(largestpalin)

print("Largest palindrome made from two 3-digit number product:", genNumbers())