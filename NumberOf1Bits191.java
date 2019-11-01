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
        n = Math.abs(n);
        int[] num1Bits = new int[n+1];
        boolean odd = true;
        for(int i = 1; i <= n; i++) {
            if(odd) {
                num1Bits[i] = num1Bits[i-1] + 1;
                odd = false;
            }
            else {
                num1Bits[i] = num1Bits[i/2];
                odd = true;
            }
        }
        return num1Bits[n];
    }
}