import java.util.Stack;

/**
 * URL of problem:
 * https://leetcode.com/problems/range-sum-of-bst/
 */

public class RangeSumBST938 {
    public static void main(String[] args) {
        Solution938 sol = new Solution938();
        TreeNode root = new TreeNode(0);
        int L = -1; int R = -1;
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
        int rangeSum = 0;
        /**
         * tree is explored using DFS
         */
        Stack<TreeNode> stack = new Stack<TreeNode>();
        stack.push(root);
        while(!stack.isEmpty()) {
            TreeNode node = stack.pop();
            if(node == null) {
                continue;
            }
            if(L <= node.val && node.val <= R) {
                rangeSum += node.val;
            }
            /**
             * if R is greater, then there
             * might be children who are
             * smaller than R as well
             */
            if(R > node.val) {
                stack.push(node.right);
            }
            /**
             * if L is smaller, then there
             * might be children who are
             * larger than L as well
             */
            if(L < node.val) {
                stack.push(node.left);
            }
        }
        return rangeSum;
    }
}