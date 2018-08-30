"""
URL of problem: https://leetcode.com/problems/array-partition-i/description/
"""

def main(nums):
    # the way to achieve the
    # maximum sum is to -
    # sort the numbers and take
    # the sum of alternate numbers
    # starting from the very first number

    # our ideal sum would have been the
    # sum of the second set of n numbers.
    # but that cannot be achieved with the
    # given criteria so this way allows us
    # to get half of those second set of n
    # numbers and the other half comes from
    # the first set of n numbers
    sorted_nums = sorted(nums)
    max_sum = 0
    length = int(len(sorted_nums)/2)
    for i in range(length):
        max_sum += sorted_nums[2*i]

    print("Maximum sum:", max_sum)
    # return max_sum

if __name__ == '__main__':
    main([1, 4, 3, 2])
