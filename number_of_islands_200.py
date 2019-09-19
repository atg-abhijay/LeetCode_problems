"""
URL of problem:
https://leetcode.com/problems/number-of-islands/
"""

from typing import List


class GridPiece(object):
    def __init__(self, is_land, row, column):
        self.is_land = is_land
        self.row = row
        self.column = column
        self.island_number = 0


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        pieces: List[List[GridPiece]] = []
        total_islands = 0
        for i, row in enumerate(grid):
            pieces.append([])
            for j, piece in enumerate(row):
                pieces[i].append(GridPiece(int(piece), i, j))

        for row in pieces:
            for piece in row:
                if self.shouldVisit(piece):
                    total_islands += 1
                    piece.island_number = total_islands
                    self.visitNeighbours(pieces, piece)

        return total_islands

    def visitNeighbours(self, pieces: List[List[GridPiece]], src_piece: GridPiece):
        src_row, src_col = src_piece.row, src_piece.column
        last_row_idx, last_col_idx = len(pieces)-1, len(pieces[0])-1

        for row_diff, col_diff in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            if 0 <= src_row+row_diff <= last_row_idx and 0 <= src_col+col_diff <= last_col_idx:
                nb_piece = pieces[src_row+row_diff][src_col+col_diff]
                if(self.shouldVisit(nb_piece)):
                    nb_piece.island_number = src_piece.island_number
                    self.visitNeighbours(pieces, nb_piece)

    def shouldVisit(self, piece: GridPiece):
        if piece.is_land and not piece.island_number:
            return True

        return False


def main():
    print(Solution().numIslands([["1", "1", "0", "0", "0"], [
          "1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))


if __name__ == '__main__':
    main()
