/**
 * URL of problem:
 * https://leetcode.com/problems/squares-of-a-sorted-array/
 */

public class SquaresOfSortedArray977 {
    public static void main(String[] args) {
        Solution977 sol = new Solution977();
        int[] A = {};
        int[] squares = sol.sortedSquares(A);
        for(int i = 0; i < squares.length; i++) {
            System.out.println(squares[i] + " ");
        }
    }
}

class Solution977 {
    public int[] sortedSquares(int[] A) {
        return new int[] {-1};
    }
}