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


if __name__ == '__main__':
    main([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
