/*
 * URL of problem:
 * https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
 */

// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

public class BSTtoGreaterSumTree1038 {
    public static void main(String[] args) {
        return;
    }
}

class Solution1038 {
    public TreeNode bstToGst(TreeNode root) {
        reverseInOrderTraversal(root, 0);
        return root;
    }

    private static int reverseInOrderTraversal(TreeNode currentNode, int valToAdd) {
        if(currentNode.right != null) {
            valToAdd = reverseInOrderTraversal(currentNode.right, valToAdd);
        }
        currentNode.val += valToAdd;
        if(currentNode.left != null) {
            valToAdd = reverseInOrderTraversal(currentNode.left, currentNode.val);
            return valToAdd;
        }
        return currentNode.val;
    }
}