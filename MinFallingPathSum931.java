import java.util.Arrays;
import java.util.Collections;

/**
 * URL of problem:
 * https://leetcode.com/problems/minimum-falling-path-sum/
 */

public class MinFallingPathSum931 {
    public static void main(String[] args) {
        Solution931 sol = new Solution931();
        int[][] A = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
        int minSum = sol.minFallingPathSum(A);
        System.out.println(minSum);
    }
}

class Solution931 {
    public int minFallingPathSum(int[][] A) {
        int numRows = A.length;
        int numColumns = A.length+2;
        /**
         * construct a new array that will
         * store the minimum cost to get
         * to a point (i,j) in the array
         *
         * the cost for the first row will
         * be the values in the first row
         * itself since it is the starting point
         */
        Integer[][] minSums = new Integer[numRows][numColumns];
        for(int j = 1; j < numColumns-1; j++) {
            minSums[0][j] = A[0][j-1];
        }
        /**
         * add dummy values before the first minimum
         * and after the last minimum so that we don't
         * have to check if we are going out of
         * bounds while iterating
         */
        for(int i = 0; i < numRows; i++) {
            minSums[i][0] = 5000;
            minSums[i][numColumns-1] = 5000;
        }

        for(int i = 1; i < numRows; i++) {
            for(int j = 1; j < numColumns-1; j++) {
                /**
                 * the minimum cost to get to (i,j) will be
                 * A[i][j-1] (j-1 to accomodate for extra column
                 * before) and minimum cost to get to points
                 * NW, North and NE to (i,j)
                 */
                minSums[i][j] = A[i][j-1] + Math.min(minSums[i-1][j-1],
                Math.min(minSums[i-1][j], minSums[i-1][j+1]));
            }
        }
        /**
         * minimum cost falling path will be minimum
         * value amongst those from the last row
         */
        return Collections.min(Arrays.asList(minSums[numRows-1]));
    }
}