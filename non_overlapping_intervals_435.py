"""
URL of problem:
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3425/
https://leetcode.com/problems/non-overlapping-intervals/
"""


class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0

        # sort the intervals by their finishing times
        intervals.sort(key=lambda x: x[1])
        predecessors = []

        # set the most recent (amongst the indexes)
        # non-overlapping interval as the predecessor
        for idx, intvl in enumerate(intervals):
            predc_idx = idx - 1
            while predc_idx > -1:
                if intervals[predc_idx][1] <= intvl[0]:
                    break
                predc_idx -= 1

            predecessors.append(predc_idx)

        # val at index i will denote max number of compatible
        # intervals upto, and including, the ith interval
        max_num_compatible = []
        for idx, intvl in enumerate(intervals):
            if predecessors[idx] == -1:
                pred_value = 0
            else:
                pred_value = max_num_compatible[predecessors[idx]]

            if idx - 1 < 0:
                previous_max = 0
            else:
                previous_max = max_num_compatible[idx-1]

            # the inclusion of each interval increases the
            # value by 1. if intvl is included, add 1 and get
            # the value of the predecessor. else, get the previous max.
            max_num_compatible.append(max(1 + pred_value, previous_max))

        # last value is the max #compatible wrt all the
        # intervals. the difference here will be the
        # no. of intervals that were excluded - aka the
        # min number of intervals to remove.
        return len(intervals) - max_num_compatible[-1]


def main():
    print(Solution().eraseOverlapIntervals(
        [[1, 2], [2, 3], [3, 4], [1, 3]]
    ))


if __name__ == '__main__':
    main()
