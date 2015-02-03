__author__ = 'Brian Rieder'

# Problem 31: Coin Sums

# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

# Answer: 73682

# This will cause immense recursion depth or stack overflow, so should not be used
def recursively_calculate_num_combinations(remaining):
    if remaining < 0:
        return
    if remaining == 0:
        global combinations
        combinations += 1
        return
    recursively_calculate_num_combinations(remaining - 1)
    recursively_calculate_num_combinations(remaining - 2)
    recursively_calculate_num_combinations(remaining - 5)
    recursively_calculate_num_combinations(remaining - 10)
    recursively_calculate_num_combinations(remaining - 20)
    recursively_calculate_num_combinations(remaining - 50)
    recursively_calculate_num_combinations(remaining - 100)
    recursively_calculate_num_combinations(remaining - 200)


def iteratively_calculate_num_combinations(amount):
    number_of_ways = [0] * (amount + 1)
    number_of_ways[0] = 1
    for coin_value in [1, 2, 5, 10, 20, 50, 100, 200]:
        for index in range(coin_value, (amount + 1)):
            number_of_ways[index] += number_of_ways[index - coin_value]
    print(number_of_ways[amount])


if __name__ == "__main__":
    breakdown_amount = int(float(input("Break down what amount of currency (£): ")) * 100)
    combinations = 0
    iteratively_calculate_num_combinations(breakdown_amount)
