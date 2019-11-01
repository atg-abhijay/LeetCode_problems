/**
 * URL of problem:
 * https://leetcode.com/problems/power-of-three/
 * Java-specific fast solution -
 * Approach 4: Integer Limitations
 * https://leetcode.com/problems/power-of-three/solution/
 */

public class PowerOfThree326 {
    public static void main(String[] args) {
        Solution326 sol = new Solution326();
        System.out.println(sol.isPowerOfThree(45));
    }
}

class Solution326 {
    public boolean isPowerOfThree(int n) {
        if(n < 1) {
            return false;
        }
        while(n > 1) {
            if(n % 3 != 0) {
                return false;
            }
            n = n/3;
        }
        return true;
    }
}