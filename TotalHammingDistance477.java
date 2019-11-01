/**
 * URL of problem:
 * https://leetcode.com/problems/total-hamming-distance/
 */

public class TotalHammingDistance477 {
    public static void main(String[] args) {
        Solution477 sol = new Solution477();
        int[] nums = new int[]{4, 14, 2};
        System.out.println(sol.totalHammingDistance(nums));
    }
}

class Solution477 {
    public int totalHammingDistance(int[] nums) {
        int hammingDistance = 0;
        for(int i = 0; i < nums.length-1; i++) {
            for(int j = i; j < nums.length; j++) {
                int xorResult = nums[i] ^ nums[j];
                while(xorResult > 0) {
                    hammingDistance += xorResult & 1;
                    xorResult = xorResult >> 1;
                }
            }
        }
        return hammingDistance;
    }
}