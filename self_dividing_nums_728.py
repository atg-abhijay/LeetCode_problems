"""
URL of problem: https://leetcode.com/problems/self-dividing-numbers/description/
"""

def main(left, right):
    nums = list(range(left, right+1))
    acceptable_nums = []
    for num in nums:
        str_num = str(num)
        initiate_continue = False
        for digit in str_num:
            if digit == '0':
                initiate_continue = True
                break

        if initiate_continue:
            continue

        self_dividing = True
        for digit in str_num:
            if num % int(digit) != 0:
                self_dividing = False
                break

        if self_dividing:
            acceptable_nums.append(num)

    print(acceptable_nums)
    # return acceptable_nums


def test():
    num = 24534630436
    str_num = str(num)
    # if 0 in str_num:
    #     print(True)
    # else:
    #     print(False)
    for digit in str_num:
        print(digit)
        if digit == 0:
            print(True)


if __name__ == '__main__':
    main(int(input("Give lower bound: ")), int(input("Give upper bound: ")))
    # main(1, 22)