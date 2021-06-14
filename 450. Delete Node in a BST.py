'''
https://leetcode.com/problems/delete-node-in-a-bst/
Given a root node reference of a BST and a key, delete the node with the given key in the BST. 
Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:
Search for a node to remove.
If the node is found, delete the node.

Example 1:
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
'''
'''
Time:O(lgn)
Space:O(H)
'''
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root == None:
            return None
        if root.val<key:
            root.right = self.deleteNode(root.right, key)
        elif root.val>key:
            root.left = self.deleteNode(root.left, key)
        elif not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            root.val = self.findmin(root.right)
            root.right = self.deleteNode(root.right, root.val)
        return root
    
    def findmin(self, node):
        while node.left:
            node = node.left
        return node.val
