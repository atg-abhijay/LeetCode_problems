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
        Integer[][] minSums = new Integer[numRows][numColumns];
        for(int j = 1; j < numColumns-1; j++) {
            minSums[0][j] = A[0][j-1];
        }
        for(int i = 0; i < numRows; i++) {
            minSums[i][0] = 5000;
            minSums[i][numColumns-1] = 5000;
        }

        for(int i = 1; i < numRows; i++) {
            for(int j = 1; j < numColumns-1; j++) {
                minSums[i][j] = A[i][j-1] + Math.min(minSums[i-1][j-1],
                Math.min(minSums[i-1][j], minSums[i-1][j+1]));
            }
        }
        return Collections.min(Arrays.asList(minSums[numRows-1]));
    }
}