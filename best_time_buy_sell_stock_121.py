"""
URL of problem:
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i, purchase_price in enumerate(prices[:-1]):
            j = i+1
            for sell_price in prices[i+1:]:
                if sell_price - purchase_price > max_profit:
                    max_profit = sell_price - purchase_price

        return max_profit


def main():
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))


if __name__ == '__main__':
    main()
