"""
URL of problem:
https://leetcode.com/problems/island-perimeter/description/
"""


def main(grid):
    # adding water cells/blocks around
    # the entire grid. now, we don't have
    # to check edge cases where there isn't
    # a block adjacent to another block.
    for i in range(len(grid)):
        grid[i] = [0] + grid[i] + [0]

    row_length = len(grid[0])
    row_water = [0 for x in range(row_length)]
    grid = [row_water] + grid + [row_water]

    perimeter = 0
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[0])-1):
            # if the cell is land
            if grid[i][j] == 1:
                # if the land is surrounded
                # by water, increment perimeter
                if grid[i-1][j] == 0:
                    perimeter += 1
                if grid[i][j+1] == 0:
                    perimeter += 1
                if grid[i][j-1] == 0:
                    perimeter += 1
                if grid[i+1][j] == 0:
                    perimeter += 1

    print(perimeter)
    # return perimeter


if __name__ == '__main__':
    main([[0, 1, 0, 0],
          [1, 1, 1, 0],
          [0, 1, 0, 0],
          [1, 1, 0, 0]])
