/**
 * URL of problem:
 * https://leetcode.com/problems/power-of-four/
 */

public class PowerOfFour342 {
    public static void main(String[] args) {
        Solution342 sol = new Solution342();
        System.out.println(sol.isPowerOfFour(5));
    }
}

class Solution342 {
    public boolean isPowerOfFour(int num) {
        if(num < 1) {
            return false;
        }
        int numBinary = num;
        while(numBinary > 1) {
            if((numBinary & 11) != 0) {
                return false;
            }
            numBinary = numBinary >> 2;
        }
        return true;
    }
}