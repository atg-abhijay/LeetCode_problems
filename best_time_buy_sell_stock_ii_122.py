"""
URL of problem:
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        trsac_profit = 0
        transaction_profits = []
        is_tp_appended = False
        purchase_price = prices[0]
        for idx, selling_price in enumerate(prices):
            # start a new transaction
            # if SP < PP or SP < previous SP -
            # the idea being to collect as many
            # transactions as possible and selecting
            # the best ones at the end.
            if selling_price < purchase_price or (idx > 0 and selling_price < prices[idx-1]):
                purchase_price = selling_price
                transaction_profits.append(trsac_profit)
                is_tp_appended = True
                trsac_profit = 0
            else:
                if selling_price - purchase_price > trsac_profit:
                    trsac_profit = selling_price - purchase_price

                is_tp_appended = False

        # in case the last transaction
        # profit hasn't been appended
        if not is_tp_appended:
            transaction_profits.append(trsac_profit)

        return sum(transaction_profits)


def main():
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))


if __name__ == '__main__':
    main()
