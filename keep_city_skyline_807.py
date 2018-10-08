"""
URL of problem:
https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/
"""


def main(grid):
    skyline_by_rows = []
    skyline_by_cols = []
    grid_length = len(grid)

    for row in grid:
        skyline_by_rows.append(max(row))

    grid_transpose = [[0 for x in range(grid_length)]
                      for y in range(grid_length)]

    for i in range(grid_length):
        row = grid[i]
        for j in range(grid_length):
            grid_transpose[j][i] = row[j]

    for row in grid_transpose:
        skyline_by_cols.append(max(row))

    # print(grid_transpose)
    max_increase = 0
    for i in range(grid_length):
        for j in range(grid_length):
            row_max = skyline_by_rows[i]
            col_max = skyline_by_cols[j]
            max_increase += min(row_max, col_max) - grid[i][j]
            grid[i][j] = min(row_max, col_max)

    print(max_increase)

if __name__ == '__main__':
    main([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]])
