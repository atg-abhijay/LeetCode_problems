"""
URL of problem:
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3418/
https://leetcode.com/problems/rotting-oranges/
"""


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Surround existing grid with empty cells
        # to avoid having to handle grid edge cases
        num_rows = len(grid)
        num_cols = len(grid[0])

        for i in range(num_rows):
            grid[i] = [0] + grid[i] + [0]

        empty_row = [0 for x in range(num_cols + 2)]
        grid = [empty_row] + grid + [empty_row]

        rotten_idxs = []
        for i in range(1, num_rows + 1):
            for j in range(1, num_cols + 1):
                if grid[i][j] == 2:
                    rotten_idxs.append([i, j])

        # Run a BFS from EACH rotten orange. Each
        # time a level is explored AND at least
        # one orange is made rotten as a result
        # overall, increment the minutes elapsed.
        minutes_elapsed = 0
        should_stop = False
        while not should_stop:
            new_idxs = []
            did_spoil_this_turn = False
            # The entire list of indexes is
            # explored within the same 1 minute.
            for position in rotten_idxs:
                tmp_result = self.rottenTheNeighbours(grid, position, new_idxs)
                did_spoil_this_turn = did_spoil_this_turn or tmp_result

            if did_spoil_this_turn:
                minutes_elapsed += 1
                rotten_idxs = new_idxs

            else:
                should_stop = True

        # If there are any fresh oranges left
        # at the end, then it is impossible
        # to rotten all of them.
        for i in range(1, num_rows + 1):
            for j in range(1, num_cols + 1):
                if grid[i][j] == 1:
                    return -1

        return minutes_elapsed

    def rottenTheNeighbours(self, grid, position, new_idxs):
        row_idx = position[0]
        col_idx = position[1]
        did_spoil_this_turn = False

        # West
        if grid[row_idx][col_idx-1] == 1:
            grid[row_idx][col_idx-1] = 2
            new_idxs.append([row_idx, col_idx-1])
            did_spoil_this_turn = True

        # North
        if grid[row_idx-1][col_idx] == 1:
            grid[row_idx-1][col_idx] = 2
            new_idxs.append([row_idx-1, col_idx])
            did_spoil_this_turn = True

        # South
        if grid[row_idx+1][col_idx] == 1:
            grid[row_idx+1][col_idx] = 2
            new_idxs.append([row_idx+1, col_idx])
            did_spoil_this_turn = True

        # East
        if grid[row_idx][col_idx+1] == 1:
            grid[row_idx][col_idx+1] = 2
            new_idxs.append([row_idx, col_idx+1])
            did_spoil_this_turn = True

        return did_spoil_this_turn


def main():
    print(Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))


if __name__ == '__main__':
    main()
