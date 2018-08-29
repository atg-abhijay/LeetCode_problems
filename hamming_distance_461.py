"""
URL of problem: https://leetcode.com/problems/hamming-distance/description/
"""

def main(x, y):
    bin_x = int(bin(x), 2)
    bin_y = int(bin(y), 2)
    xor_result = bin(bin_x ^ bin_y)
    hamming_dist = 0
    for digit in xor_result:
        if digit == '1':
            hamming_dist += 1

    # print("Hamming distance:", hamming_dist)
    return hamming_dist

main(int(input("Give first number: ")), int(input("Give second number: ")))
