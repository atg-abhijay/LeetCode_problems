"""
URL of problem:
https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/
"""


def main(grid):
    # skyline values by columns
    skyline_by_cols = []
    grid_length = len(grid)

    # making a transpose of the grid
    grid_transpose = [[0 for x in range(grid_length)]
                      for y in range(grid_length)]

    for i in range(grid_length):
        row = grid[i]
        for j in range(grid_length):
            grid_transpose[j][i] = row[j]

    # adding skyline by column values
    for row in grid_transpose:
        skyline_by_cols.append(max(row))

    max_increase = 0
    for i in range(grid_length):
        row_max = max(grid[i])
        for j in range(grid_length):
            col_max = skyline_by_cols[j]
            # the grid value at the max can be the minimum
            # amongst the skyline row and column value
            # at that intersection
            max_increase += min(row_max, col_max) - grid[i][j]
            grid[i][j] = min(row_max, col_max)

    print(max_increase)
    # return max_increase


if __name__ == '__main__':
    main([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]])
