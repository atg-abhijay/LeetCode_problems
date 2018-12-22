/**
 * URL of problem:
 * https://leetcode.com/problems/climbing-stairs/
*/

public class ClimbingStairs70 {
    public static void main(String[] args) {
        Solution70 sol = new Solution70();
        System.out.println(sol.climbStairs(3));
    }
}

class Solution70 {
    public int climbStairs(int n) {
        int[] numWays = new int[n+1];
        numWays[0] = 1;
        numWays[1] = 1;
        if(n == 1) {
            return 1;
        }
        for(int i = 2; i < n+1; i++) {
            numWays[i] = numWays[i-2] + numWays[i-1];
        }
        return numWays[n];
    }
}
