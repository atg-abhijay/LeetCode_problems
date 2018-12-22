import java.util.ArrayDeque;
import java.util.Queue;

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
        Queue<TreeNode> q = new ArrayDeque<TreeNode>();
        q.add(root);
        while(!q.isEmpty()) {
            TreeNode node = q.poll();
            if(L <= node.val && node.val <= R) {
                rangeSum += node.val;
            }
            if(node.left != null ) {
                q.add(node.left);
            }
            if(node.right != null) {
                q.add(node.right);
            }
        }
        return rangeSum;
    }
}