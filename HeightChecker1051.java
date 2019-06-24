import java.util.Arrays;

/**
 * URL of problem:
 * https://leetcode.com/problems/height-checker/
 */

public class HeightChecker1051 {
    public static void main(String[] args){
        Solution1051 sol = new Solution1051();
        int[] heights = {1,1,4,2,1,3};
        System.out.println(sol.heightChecker(heights));
    }
}

class Solution1051 {
    public int heightChecker(int[] heights) {
        int numElements = heights.length;
        int[] copyOFHeights = Arrays.copyOf(heights, numElements);
        Arrays.sort(copyOFHeights);
        int numOutOfPlace = 0;
        for(int i = 0; i < numElements; i++) {
            if(heights[i] != copyOFHeights[i]) {
                numOutOfPlace++;
            }
        }
        return numOutOfPlace;
    }
}
