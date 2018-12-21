"""
URL of problem:
https://leetcode.com/problems/counting-bits/
"""


def main(num):
    numBits = [0]
    odd = True
    for i in range(1, num+1):
        if odd:
            numBits.append(numBits[-1] + 1)
            odd = False
        else:
            numBits.append(numBits[int(i/2)])
            odd = True

    # print(numBits)
    return numBits


if __name__ == '__main__':
    main(12)
