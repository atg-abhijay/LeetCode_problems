"""
URL of problem:
https://leetcode.com/problems/judge-route-circle/description/
"""


def main(moves):
    moves_list = list(moves)
    x = 0
    y = 0
    for move in moves_list:
        if move == 'U':
            y += 1
        elif move == 'D':
            y -= 1
        elif move == 'R':
            x += 1
        elif move == 'L':
            x -= 1

    # if both x and y are 0,
    # then we are at the origin
    if x == 0 and y == 0:
        # print("True")
        return True

    # print("False")
    return False


if __name__ == '__main__':
    main(input("Give input string for moves: "))
