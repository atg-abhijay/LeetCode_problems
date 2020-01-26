"""
URL of problem:
https://leetcode.com/problems/find-the-town-judge/
"""


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust:
            return 1

        trust_scores = [0 for x in range(N+1)]
        for pair in trust:
            trust_scores[pair[0]] -= 1
            trust_scores[pair[1]] += 1

        for index, score in enumerate(trust_scores):
            if score == N-1:
                return index

        return -1
