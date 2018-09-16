"""
URL of problem:
https://leetcode.com/problems/self-dividing-numbers/description/
"""


def main(left, right):
    nums = list(range(left, right+1))
    acceptable_nums = []
    for num in nums:
        str_num = str(num)
        # boolean value to decide whether
        # to skip the current number if
        # it contains the digit 0 in it
        initiate_continue = False
        for digit in str_num:
            if digit == '0':
                initiate_continue = True
                # if there is a zero in the
                # number, we can break out of
                # this innermost loop since
                # we don't have to check further
                break

        # if the var was set to True,
        # then we skip the current
        # number in the list
        if initiate_continue:
            continue

        # only those numbers proceed
        # to this point that do not
        # contain a zero in them.

        # boolean value to see if
        # the number is self-dividing
        self_dividing = True
        for digit in str_num:
            if num % int(digit) != 0:
                # if the remainder is not zero in
                # any one of the iterations, we
                # set the boolean to False and
                # break since we don't need to check further
                self_dividing = False
                break

        if self_dividing:
            # if number is self-dividing,
            # then it is an acceptable number
            acceptable_nums.append(num)

    print(acceptable_nums)
    # return acceptable_nums


if __name__ == '__main__':
    main(int(input("Give lower bound: ")), int(input("Give upper bound: ")))
