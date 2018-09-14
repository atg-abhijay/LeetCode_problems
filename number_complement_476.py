"""
URL of problem:
https://leetcode.com/problems/number-complement/description/
"""


def main(num):
    bin_num = bin(num)[2:]
    # print(bin_num)
    complement_list = [1 - int(digit) for digit in bin_num]
    # print(complement_list)
    complement_list.reverse()
    complement = 0
    for power, bit in enumerate(complement_list):
        if bit != 0:
            complement += 2**power

    # print("Complement:", complement)
    return complement


if __name__ == '__main__':
    main(int(input("Enter a number: ")))
