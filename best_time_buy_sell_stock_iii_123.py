"""
URL of problem:
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/551/week-3-august-15th-august-21st/3426/
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
"""

from collections import deque


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

        transactions = self.generateAllTransactions(prices)
        if not transactions:
            return 0

        # Sort the transactions by their sell indexes
        # and find the most recent non-overlapping
        # predecessor transaction for each transaction
        transactions.sort(key=lambda t: t.sell_idx)
        pred_trn_idxs = []
        for idx, t in enumerate(transactions):
            pred_idx = idx - 1
            while pred_idx > -1:
                if transactions[pred_idx].sell_idx < t.pchse_idx:
                    break
                pred_idx -= 1

            pred_trn_idxs.append(pred_idx)

        max_profits = []
        for idx, t in enumerate(transactions):
            if pred_trn_idxs[idx] == -1:
                pred_value = 0
            else:
                # pred_value = max_profits[pred_trn_idxs[idx]]
                pred_value = self.findMaxProfitTransaction(
                    transactions, pred_trn_idxs[idx])

            if idx - 1 < 0:
                previous_max = 0
            else:
                previous_max = max_profits[idx-1]

            max_profits.append(max(t.profit + pred_value, previous_max))

        # best_trns = self.findBestTransactions(
        #     len(transactions)-1, transactions, pred_trn_idxs, max_profits)

        # return self.maxProfitFromBestKTransactions(2, best_trns)
        return max_profits[-1]

    def generateAllTransactions(self, prices):
        """
        :type prices: List[int]
        :rtype: List[Transaction]
        """
        transactions = []
        prices_queue = deque([(0, prices[0])])
        idx_in_queue = [0 for x in range(len(prices))]
        while prices_queue:
            trsac_profit = 0
            pp_idx, purchase_price = prices_queue.popleft()
            for sp_idx, sell_price in enumerate(prices[pp_idx+1:]):
                sp_idx = sp_idx + pp_idx + 1
                condn_a = sell_price <= purchase_price
                condn_b = sp_idx > 0 and sell_price < prices[sp_idx-1]
                if condn_a:
                    if not idx_in_queue[sp_idx]:
                        prices_queue.append((sp_idx, sell_price))
                        idx_in_queue[sp_idx] = 1
                    break

                elif condn_b and not idx_in_queue[sp_idx]:
                    idx_in_queue[sp_idx] = 1
                    prices_queue.append((sp_idx, sell_price))

                elif sell_price - purchase_price > trsac_profit:
                    trsac_profit = sell_price - purchase_price
                    transactions.append(Transaction(
                        pp_idx, sp_idx, trsac_profit))

        return transactions

    def findMaxProfitTransaction(self, transactions, last_idx):
        max_profit_so_far = 0
        for t in transactions[:last_idx+1]:
            if t.profit > max_profit_so_far:
                max_profit_so_far = t.profit

        return max_profit_so_far

    # def maxProfitFromBestKTransactions(self, k, best_trns):
    #     best_trns.sort(key=lambda t: t.profit)
    #     max_profit = 0
    #     while k > 0 and best_trns:
    #         max_profit += best_trns.pop().profit
    #         k -= 1

    #     return max_profit

    # def findBestTransactions(self, idx, transactions, pred_trn_idxs, max_profits):
    #     if idx < 0:
    #         return []

    #     elif transactions[idx].profit + transactions[pred_trn_idxs[idx]].profit > max_profits[idx-1]:
    #         return [transactions[idx]] + self.findBestTransactions(pred_trn_idxs[idx], transactions, pred_trn_idxs, max_profits)

    #     else:
    #         return self.findBestTransactions(idx-1, transactions, pred_trn_idxs, max_profits)


def main():
    print(Solution().maxProfit(
        [6, 5, 4, 8, 6, 8, 7, 8, 9, 4, 5]
    ))


if __name__ == '__main__':
    main()
