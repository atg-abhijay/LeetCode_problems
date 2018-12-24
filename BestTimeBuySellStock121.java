/**
 * URL of problem:
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
 */

public class BestTimeBuySellStock121 {
    public static void main(String[] args) {
        Solution121 sol = new Solution121();
        int[] prices = {7, 1, 5, 3, 6 ,4};
        System.out.println(sol.maxProfit(prices));
    }
}

class Solution121 {
    public int maxProfit(int[] prices) {
        if(prices.length == 0) {
            return 0;
        }
        int arrSize = prices.length;
        int[] bestProfit = new int[arrSize];
        bestProfit[0] = -1*prices[0];
        int dayShouldBuy = 0;
        for(int i = 1; i < arrSize; i++) {
            int buyToday = -1*prices[i];
            int sellToday = -1*prices[dayShouldBuy] + prices[i];
            int doNothing = bestProfit[i-1];
            if(buyToday >= sellToday && buyToday >= doNothing) {
                dayShouldBuy = i;
                bestProfit[i] = buyToday;
            }
            else {
                bestProfit[i] = Math.max(buyToday, Math.max(sellToday, doNothing));
            }

            if(sellToday > buyToday && sellToday > doNothing && sellToday < 0) {
                bestProfit[i] = buyToday;
                dayShouldBuy = i;
            }
        }
        return Math.max(0, bestProfit[arrSize-1]);
    }
}