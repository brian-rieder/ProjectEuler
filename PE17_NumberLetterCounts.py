__author__ = 'Brian Rieder'

# Problem 17: Number Letter Counts

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
# letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# Answer: 21124

single = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
decimal = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]
hundred = 7
thousand = 8

total = 0
max_val = 5

# Cover all of the 1 - 19s
for i in range(0, 20):
    total += single[i]

total *= 9

# Cover all decimal values
for i in range(0, 10):
    total += decimal[i] * 100

total += hundred * 900

total += thousand

print(total)