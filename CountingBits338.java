/**
 * URL of problem:
 * https://leetcode.com/problems/counting-bits/
 */

public class CountingBits338 {
    public static void main(String[] args) {
        Solution338 sol = new Solution338();
        int[] numBits = sol.countBits(Integer.parseInt(args[0]));
        for(int i = 0; i < numBits.length; i++) {
            System.out.print(numBits[i] + " ");
        }
        System.out.println();
    }
}

class Solution338 {
    public int[] countBits(int num) {
        int[] numBits = new int[num+1];
        boolean odd = true;
        for(int i = 1; i <= num; i++) {
            /**
             * if i is odd, it's #1bits is
             * (1 + #1bits in the previous number)
             */
            if(odd) {
                numBits[i] = numBits[i-1] + 1;
                odd = false;
            }
            /**
             * if i is even, it can be obtained
             * by (i/2)*2, which doesn't add
             * any extra 1 bits to i
             */
            else {
                numBits[i] = numBits[i/2];
                odd = true;
            }
        }
        return numBits;
    }
}