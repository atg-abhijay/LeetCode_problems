"""
URL of problem: https://leetcode.com/problems/hamming-distance/description/
"""

def main(x, y):
    xor_result = x ^ y
    # converting result to binary
    # and getting rid of the '0b'
    # at the beginning of the number
    xor_result = bin(xor_result)[2:]
    hamming_dist = 0
    for digit in xor_result:
        if digit == '1':
            hamming_dist += 1

    # print("Hamming distance:", hamming_dist)
    return hamming_dist


main(int(input("Give first number: ")), int(input("Give second number: ")))
