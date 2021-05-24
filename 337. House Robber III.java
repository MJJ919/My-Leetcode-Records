/*
https://leetcode.com/problems/house-robber-iii/
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.
Besides the root, each house has one and only one parent house. 
After a tour, the smart thief realized that all houses in this place form a binary tree. 
It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

Example 1:
Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
*/
/*
The faster way.
*/
class Solution {
    public int rob(TreeNode root) {
        int[] res = sub(root);
        return Math.max(res[0], res[1]);
    }
    
    public int[] sub(TreeNode node){
        if (node==null) return new int[2];
        int[] left = sub(node.left);
        int[] right = sub(node.right);
        int[] res = new int[2];
        res[0] = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
        res[1] = node.val + left[0] + right[0];
        return res;
    }
}
/*
Time:O(n)
Space:O(n)
*/
class Solution {
    public int rob(TreeNode root) {
        return sub(root, new HashMap<>());
    }
    
    public int sub(TreeNode node, HashMap<TreeNode, Integer> map){
        if (node==null) return 0;
        if (map.containsKey(node))  return map.get(node);
        int val = 0;
        if (node.left!=null)    val += sub(node.left.left, map)+sub(node.left.right, map);
        if (node.right!=null)   val += sub(node.right.left, map)+sub(node.right.right, map);
        int res = Math.max(node.val+val, sub(node.left, map)+sub(node.right, map));
        map.put(node, res);
        return res;
    }
}
