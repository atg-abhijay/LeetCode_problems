/**
 * URL of problem:
 * https://leetcode.com/problems/range-sum-of-bst/
 */

public class RangeSumBST938 {
    public static void main(String[] args) {
        Solution938 sol = new Solution938();
        int rangeSum = sol.rangeSumBST(root, L, R);
        System.out.println(rangeSum);
    }
}

// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

class Solution938 {
    public int rangeSumBST(TreeNode root, int L, int R) {
        return -1;
    }
}