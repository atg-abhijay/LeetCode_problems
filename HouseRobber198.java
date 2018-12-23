/**
 * URL of problem:
 * https://leetcode.com/problems/house-robber/
 */

public class HouseRobber198 {
    public static void main(String[] args) {
        Solution198 sol = new Solution198();
        int[] nums = {2, 7, 9, 3, 1};
        System.out.println(sol.rob(nums));
    }
}

class Solution198 {
    public int rob(int[] nums) {
        if(nums.length == 0) {
            return 0;
        }
        int[] maxAmountRob = new int[nums.length+1];
        maxAmountRob[0] = 0;
        maxAmountRob[1] = nums[0];
        for(int i = 2; i < maxAmountRob.length; i++) {
            maxAmountRob[i] = Math.max(maxAmountRob[i-1], nums[i-1] + maxAmountRob[i-2]);
        }
        return maxAmountRob[maxAmountRob.length-1];
    }
}