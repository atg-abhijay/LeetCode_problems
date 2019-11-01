/**
 * URL of problem:
 * https://leetcode.com/problems/power-of-two/
 */

public class PowerOfTwo231 {
    public static void main(String[] args){
        Solution231 sol = new Solution231();
        System.out.println(sol.isPowerOfTwo(218));
    }
}

class Solution231 {
    public boolean isPowerOfTwo(int n) {
        if(n < 1) {
            return false;
        }
        /**
         * Powers of two are of the form:
         * '1' followed by x number of zeroes
         * where x >= 0
         */
        int nBinary = n;
        int lastBit;
        while(nBinary > 1) {
            lastBit = nBinary & 1;
            if(lastBit == 1) {
                return false;
            }
            nBinary = nBinary >> 1;
        }
        return true;
    }
}