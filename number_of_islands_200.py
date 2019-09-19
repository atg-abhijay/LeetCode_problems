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

        # pprint([piece.is_land for row in pieces for piece in row])
        for row in pieces:
            for piece in row:
                if self.shouldVisit(piece):
                    total_islands += 1
                    piece.island_number = total_islands
                    self.visitNeighbours(pieces, piece)

        return total_islands

    def visitNeighbours(self, pieces: List[List[GridPiece]], src_piece: GridPiece):
        src_row, src_col = src_piece.row, src_piece.column
        if src_row != 0 and self.shouldVisit(pieces[src_row-1][src_col]):
            pieces[src_row-1][src_col].island_number = src_piece.island_number
            self.visitNeighbours(pieces, pieces[src_row-1][src_col])

        if src_col != len(pieces[0]) - 1 and self.shouldVisit(pieces[src_row][src_col+1]):
            pieces[src_row][src_col+1].island_number = src_piece.island_number
            self.visitNeighbours(pieces, pieces[src_row][src_col+1])

        if src_row != len(pieces) - 1 and self.shouldVisit(pieces[src_row+1][src_col]):
            pieces[src_row+1][src_col].island_number = src_piece.island_number
            self.visitNeighbours(pieces, pieces[src_row+1][src_col])

        if src_col != 0 and self.shouldVisit(pieces[src_row][src_col-1]):
            pieces[src_row][src_col-1].island_number = src_piece.island_number
            self.visitNeighbours(pieces, pieces[src_row][src_col-1])

    def shouldVisit(self, piece: GridPiece):
        if piece and piece.is_land and not piece.island_number:
            return True

        return False


def main():
    print(Solution().numIslands([["1", "1", "0", "0", "0"], [
          "1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))


if __name__ == '__main__':
    main()
