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
        /**
         * exploring tree with BFS. not exploring
         * some nodes as explained below
         */
        while(!q.isEmpty()) {
            TreeNode node = q.poll();
            if(L <= node.val && node.val <= R) {
                rangeSum += node.val;
            }

            /**
             * if the left child has a value
             * geq than L, we can add it to
             * the queue. if it is less than L,
             * we can only add it to the queue
             * if it has a right child
             */
            TreeNode leftChild = node.left;
            if(leftChild != null) {
                if(leftChild.val >= L) {
                    q.add(leftChild);
                }
                else {
                    if(leftChild.right != null) {
                        q.add(leftChild);
                    }
                }
            }

            /**
             * if the right child has a value
             * leq than R, then it can be added
             * to the queue. if it is greater than
             * R, it can only be added to the queue
             * if it has a left child
             */
            TreeNode rightChild = node.right;
            if(rightChild != null) {
                if(rightChild.val <= R) {
                    q.add(rightChild);
                }
                else {
                    if(rightChild.left != null) {
                        q.add(rightChild);
                    }
                }
            }
        }
        return rangeSum;
    }
}