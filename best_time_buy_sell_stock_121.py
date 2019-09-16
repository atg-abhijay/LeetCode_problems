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
        if not prices:
            return 0

        max_profit = 0
        purchase_price = prices[0]
        for selling_price in prices:
            if selling_price < purchase_price:
                purchase_price = selling_price
            else:
                if selling_price - purchase_price > max_profit:
                    max_profit = selling_price - purchase_price

        return max_profit


def main():
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))


if __name__ == '__main__':
    main()
