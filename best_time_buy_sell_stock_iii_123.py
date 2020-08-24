"""
URL of problem:
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3426/
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
"""


class Transaction(object):
    def __init__(self, pchse_idx, sell_idx, profit):
        self.pchse_idx = pchse_idx
        self.sell_idx = sell_idx
        self.profit = profit


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        transactions = self.generateAllTransactions(prices, False)
        transactions += self.generateAllTransactions(prices, True)
        if not transactions:
            return 0
        transactions.sort(key=lambda t: t.profit, reverse=True)
        best_trn = transactions[0]
        if len(transactions) > 1 and self.slicePricesAndFindProfit(prices, transactions, best_trn) == 0:
            best_trn = transactions[1]

        return best_trn.profit + self.slicePricesAndFindProfit(prices, transactions, best_trn)

    def slicePricesAndFindProfit(self, prices, transactions, best_trn):
        pchse_idxs = [t.pchse_idx for t in transactions]
        if best_trn.pchse_idx == min(pchse_idxs):
            return self.oneTransactionMaxProfit(prices[best_trn.sell_idx+1:])
        elif best_trn.pchse_idx == max(pchse_idxs):
            return self.oneTransactionMaxProfit(prices[:best_trn.pchse_idx])
        else:
            prefix_prices = prices[:best_trn.pchse_idx]
            suffix_prices = prices[best_trn.sell_idx+1:]
            return max(self.oneTransactionMaxProfit(prefix_prices), self.oneTransactionMaxProfit(suffix_prices))

    def generateAllTransactions(self, prices, is_enabled):
        """
        :type prices: List[int]
        :rtype: List[Transaction]
        """
        trsac_profit, purchase_idx, sell_idx = 0, 0, 0
        transactions = []
        is_transaction_appended = False
        purchase_price = prices[0]
        for idx, price in enumerate(prices):
            # start a new transaction
            # if price < PP or price < previous SP -
            # the idea being to collect as many
            # transactions as possible.
            if (not is_enabled and price <= purchase_price) or (is_enabled and idx > 0 and price < prices[idx-1]):
                if trsac_profit != 0:
                    transactions.append(Transaction(
                    purchase_idx, sell_idx, trsac_profit))
                    is_transaction_appended = True

                purchase_price = price
                purchase_idx = idx
                trsac_profit = 0
            else:
                if price - purchase_price > trsac_profit:
                    trsac_profit = price - purchase_price
                    sell_idx = idx

                is_transaction_appended = False

        # in case the last transaction
        # profit hasn't been appended
        if not is_transaction_appended and trsac_profit != 0:
            transactions.append(Transaction(
                purchase_idx, sell_idx, trsac_profit))

        return transactions

    def oneTransactionMaxProfit(self, prices):
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
    print(Solution().maxProfit([8, 3, 6, 2, 8, 8, 8, 4, 2, 0, 7, 2, 9, 4, 9]))


if __name__ == '__main__':
    main()
