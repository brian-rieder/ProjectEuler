__author__ = 'Brian Rieder'

# Problem 15: Lattice Paths

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are
# exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?

grid_dime = [20, 20]


def recursive_approach(grid_dimension):
    if grid_dimension == [0, 0]:
        return 1
    path_val = 0
    if grid_dimension[0] > 0:
        path_val += recursive_approach([grid_dimension[0]-1, grid_dimension[1]])
    if grid_dimension[1] > 0:
        path_val += recursive_approach([grid_dimension[0], grid_dimension[1]-1])
    return path_val


def mathematical_approach(grid_dimension):
    grid_val = [[i+1 for i in range(1, grid_dimension + 1)] for j in range(1, grid_dimension + 1)]
    for i in range(0, grid_dimension):
        grid_val[i][0] = i + 2
    for row in range(1, grid_dimension):
        for column in range(1, grid_dimension):
            grid_val[row][column] = grid_val[row - 1][column] + grid_val[row][column - 1]
    return grid_val[grid_dimension - 1][grid_dimension - 1]



result = mathematical_approach(20)

print(result)