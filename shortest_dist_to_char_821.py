"""
URL of problem:
https://leetcode.com/problems/shortest-distance-to-a-character/description/
"""


def main(string, char):
    char_positions = []
    for index, letter in enumerate(string):
        if letter == char:
            char_positions.append(index)

    char_distances = []
    for index, letter in enumerate(string):
        min_dist = len(string)
        for pos in char_positions:
            dist = abs(index - pos)
            if dist < min_dist:
                min_dist = dist

        char_distances.append(min_dist)

    print(char_distances)
    # return char_distances

if __name__ == '__main__':
    main("loveleetcode", 'e')
