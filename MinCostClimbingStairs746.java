/**
 * URL of problem:
 * https://leetcode.com/problems/min-cost-climbing-stairs/
 */

public class MinCostClimbingStairs746 {
    public static void main(String[] args) {
        Solution746 sol = new Solution746();
        int[] cost = {1, 100, 1, 1, 1, 100, 1, 1, 100, 1};
        System.out.println(sol.minCostClimbingStairs(cost));
    }
}

class Solution746 {
    public int minCostClimbingStairs(int[] cost) {
        int[] minCosts = new int[cost.length+1];
        minCosts[0] = 0;
        minCosts[1] = 0;
        for(int i = 2; i < minCosts.length; i++) {
            minCosts[i] = Math.min(cost[i-2] + minCosts[i-2], cost[i-1] + minCosts[i-1]);
        }
        return minCosts[minCosts.length-1];
    }
}