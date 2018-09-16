"""
URL of problem: https://leetcode.com/problems/jewels-and-stones/description/
"""


def main(J, S):
    num_jewels = 0
    jewels_set = set(J)
    stones_set = list(S)
    # print(jewels_set)
    for stone in stones_set:
        if stone in jewels_set:
            num_jewels += 1

    # print(num_jewels)
    return num_jewels

main(input("Give string of jewels: "), input("Give string of stones: "))
