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
            if row[j] == 'X':
                row[j] = 'A'
                num_battleships += 1
                isHorizontal = False
                j_inner = j+1
                while j_inner < num_cols:
                    if row[j_inner] == 'X':
                        row[j_inner] = 'A'
                        j_inner += 1
                        isHorizontal = True
                    else:
                        break

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
