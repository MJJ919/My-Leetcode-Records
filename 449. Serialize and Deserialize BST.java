/*
https://leetcode.com/problems/serialize-and-deserialize-bst/
Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, 
or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. 
There is no restriction on how your serialization/deserialization algorithm should work. 
You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Example 1:
Input: root = [2,1,3]
Output: [2,1,3]
*/
/*
Time:O(n)
Space:O(n)
*/
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root==null) return "none";
        return root.val+","+serialize(root.left)+","+serialize(root.right);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        LinkedList<String> l = new LinkedList<>(Arrays.asList(data.split(",")));
        return helper(l);
    }
    
    private TreeNode helper(LinkedList<String> l){
        String s = l.poll();
        if (s.equals("none"))  return null;
        TreeNode root = new TreeNode(Integer.valueOf(s));
        root.left = helper(l);
        root.right = helper(l);
        return root;
    }
}
