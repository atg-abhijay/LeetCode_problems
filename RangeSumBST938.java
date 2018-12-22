import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Stack;

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
        int rangeSum = 0;
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
            if(R > node.val) {
                stack.push(node.right);
            }
            if(L < node.val) {
                stack.push(node.left);
            }
        }
        return rangeSum;
    }
}