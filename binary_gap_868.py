"""
URL of problem:
https://leetcode.com/problems/binary-gap/description/
"""


def main(num):
    bin_num = bin(num)[2:]
    max_dist = 0
    dist_counter = -1
    encounter_start_one = False
    for digit in bin_num:
        digit = int(digit)
        if encounter_start_one:
            if digit == 1:
                dist_counter += 1
                if max_dist < dist_counter:
                    max_dist = dist_counter

                dist_counter = 0
            else:
                dist_counter += 1

        else:
            if digit == 1:
                encounter_start_one = True
                dist_counter += 1

    print("Max distance:", max_dist)


if __name__ == '__main__':
    main(int(input("Give a number: ")))
