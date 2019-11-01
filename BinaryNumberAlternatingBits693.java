/**
 * URL of problem:
 * https://leetcode.com/problems/binary-number-with-alternating-bits/
 */

public class BinaryNumberAlternatingBits693 {
    public static void main(String[] args) {
        Solution693 sol = new Solution693();
        System.out.println(sol.hasAlternatingBits(11));
    }
}

class Solution693 {
    public boolean hasAlternatingBits(int n) {
        int previousBit = n & 1;
        n = n >> 1;
        while(n > 0) {
            if(previousBit == (n & 1)) {
                return false;
            }
            previousBit = n & 1;
            n = n >> 1;
        }
        return true;
    }
}