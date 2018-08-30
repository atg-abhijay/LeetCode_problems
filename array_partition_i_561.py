"""
URL of problem: https://leetcode.com/problems/array-partition-i/description/
"""

def main(nums):
    sorted_nums = sorted(nums)
    max_sum = 0
    length = int(len(sorted_nums)/2)
    for i in range(length):
        max_sum += sorted_nums[2*i]

    print("Maximum sum:", max_sum)
    # return max_sum

if __name__ == '__main__':
    main([1, 4, 3, 2])
