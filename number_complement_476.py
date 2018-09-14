"""
URL of problem:
https://leetcode.com/problems/number-complement/description/
"""


def main(num):
    """
    main method for running the program.
    Argument:
        num - integer
    Prints:
        Complement of num, where complement strategy is
        to flip the bits of its binary representation.
    """
    # obtaining the binary representation
    # of the input number and getting rid
    # of the '0b' characters at the beginning
    bin_num = bin(num)[2:]
    # generating the complement of the
    # binary number. to get complement for
    # values of (0, 1), it suffices to use
    # 1 - value. we use int(digit) since
    # the digits are characters in bin_num
    complement_list = [1 - int(digit) for digit in bin_num]
    # have to get int representation of
    # complement binary number. we reverse
    # list so that the lowest bit gets the
    # 0th index, next bit gets 1st index and so on.
    complement_list.reverse()
    complement = 0
    # the index acts as the power to which 2
    # has to be raised. the bit decides for on/off.
    # perform transformation and obtain complement int.
    for power, bit in enumerate(complement_list):
        if bit != 0:
            complement += 2**power

    print("Complement:", complement)
    # return complement


if __name__ == '__main__':
    main(int(input("Enter a number: ")))
