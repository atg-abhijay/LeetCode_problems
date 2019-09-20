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
        # Use the given grid to create a
        # nested list of GridPiece objects
        pieces: List[List[GridPiece]] = []
        total_islands = 0
        for i, row in enumerate(grid):
            pieces.append([])
            for j, piece in enumerate(row):
                pieces[i].append(GridPiece(int(piece), i, j))

        # If there is a piece of land that is not
        # part of an island yet, assign it as the
        # first piece of a new island and run a DFS
        # from this piece to find the other pieces
        # for this island.
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

        # The diffs correspond to diffs needed to get to the North,
        # East, South and West pieces respectively from the source piece.
        # Check that the indices don't go out of bound. If the neighbouring
        # piece is land and is not part of an island yet, make it a part of
        # the same island as the source piece and run a DFS from the neighbouring piece.
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
