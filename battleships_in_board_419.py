"""
URL of problem:
https://leetcode.com/problems/battleships-in-a-board/description/
"""


def main(board):
    num_rows = len(board)
    num_cols = len(board[0])
    num_battleships = 0
    for i in range(num_rows):
        row = board[i]
        for j in range(num_cols):
            # bship = battleship
            # if the cell is marked 'X',
            # change it to 'A' and since
            # we have a bship for
            # sure, increment num_battleships.
            if row[j] == 'X':
                row[j] = 'A'
                num_battleships += 1
                # we have two possibilites now. the
                # bship might be horizontal or vertical.
                # assume it to not be horizontal. check
                # the cell to the right of the current
                # cell. if it is marked 'X' we have a
                # horizontal bship. check how long we
                # obtain X's for and mark them with A's
                # so that we don't check those cells later
                isHorizontal = False
                j_inner = j+1
                while j_inner < num_cols:
                    if row[j_inner] == 'X':
                        row[j_inner] = 'A'
                        j_inner += 1
                        isHorizontal = True
                    else:
                        break

                # if the previous loop did
                # not set isHorizontal to
                # True, then the bship is vertical.
                # follow a similar procedure as above,
                # checking cells below the current cell
                # until we stop getting X's.
                if not isHorizontal:
                    i_inner = i+1
                    while i_inner < num_rows:
                        if board[i_inner][j] == 'X':
                            board[i_inner][j] = 'A'
                            i_inner += 1
                        else:
                            break

    return num_battleships


if __name__ == '__main__':
    main([["X", "X", "X"]])
