"""
URL of problem:
https://leetcode.com/problems/reducing-dishes/
"""


class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        satisfaction.sort()
        sum_like_times = 0
        # All dishes have (zero or) positive satisfaction
        if satisfaction[0] >= 0:
            for idx, satsfn in enumerate(satisfaction):
                sum_like_times += ((idx+1) * satsfn)

            return sum_like_times

        # All dishes have negative (or zero) satisfaction
        elif satisfaction[-1] <= 0:
            return 0

        # General case
        max_value = 0
        for start_idx in range(len(satisfaction)):
            sum_like_times = 0
            for idx, satsfn in enumerate(satisfaction[start_idx:]):
                sum_like_times += ((idx+1) * satsfn)

            if sum_like_times > max_value:
                max_value = sum_like_times

        return max_value


def main():
    print(Solution().maxSatisfaction([-2, 5, -1, 0, 3, -3]))


if __name__ == '__main__':
    main()
