import java.util.Arrays;

/**
 * URL of problem:
 * https://leetcode.com/problems/squares-of-a-sorted-array/
 */

public class SquaresOfSortedArray977 {
    public static void main(String[] args) {
        Solution977 sol = new Solution977();
        int[] A = {-7,-3,2,3,11};
        int[] squares = sol.sortedSquares(A);
        for(int i = 0; i < squares.length; i++) {
            System.out.print(squares[i] + " ");
        }
        System.out.println();
    }
}

class Solution977 {
    public int[] sortedSquares(int[] A) {
        int numElements = A.length;
        int[] squares = new int[numElements];
        for(int i = 0; i < numElements; i++) {
            squares[i] = A[i] * A[i];
        }
        Arrays.sort(squares);
        return squares;
    }
}