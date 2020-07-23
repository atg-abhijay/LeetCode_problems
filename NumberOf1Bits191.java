/**
 * URL of problem:
 * https://leetcode.com/problems/number-of-1-bits/
 */

public class NumberOf1Bits191 {
    public static void main(String[] args) {
        Solution191 sol = new Solution191();
        System.out.println(sol.hammingWeight(0b11111111111111111111111111111101));
    }
}

class Solution191 {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int num1Bits = 0;
        while(n != 0) {
            num1Bits += (n & 1);
            n = n >>> 1;
        }
        return num1Bits;
    }
}