"""
URL of problem:
https://leetcode.com/problems/baseball-game/description/
"""


def main(operations):
    total_points = 0
    # list to keep track
    # of points after each op
    points = []
    for op in operations:
        if op == "+":
            new_points = points[-1] + points[-2]
            total_points += new_points
            points.append(new_points)

        elif op == "D":
            new_points = 2*points[-1]
            total_points += new_points
            points.append(new_points)

        elif op == "C":
            # subtract the last valid points
            # from the total points and remove
            # the last valid points from the list
            total_points -= points[-1]
            points.pop()

        # the last type of op
        # is a number
        else:
            total_points += int(op)
            points.append(int(op))

    # print("Total points:", total_points)
    return total_points


if __name__ == '__main__':
    main(["5", "-2", "4", "C", "D", "9", "+", "+"])
