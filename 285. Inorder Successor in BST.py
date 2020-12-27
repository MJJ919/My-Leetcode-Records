'''
https://leetcode.com/problems/inorder-successor-in-bst/
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
The successor of a node p is the node with the smallest key greater than p.val.

Example 1:
Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.

Example 2:
Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
'''
'''
Iteration
Time:O(h)
Space:O(h)
'''
class Solution(object):
    def inorderSuccessor(self, root, p):
        s, inorder = [], float('-inf')
        while True:
            while root:
                s.append(root)
                root = root.left
            if not s:
                break
            node = s.pop()
            if p.val == inorder:
                return node
            inorder = node.val
            root = node.right
       
        return None
        
'''
Recursive
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def inorderSuccessor(self, root, p):
        res = []
        self.rec(root, res)
        i = res.index(p)
        if i<len(res)-1:
            return res[i+1]
        else:
            return None
    
    def rec(self, node, res):
        if node:
            self.rec(node.left, res)
            res.append(node)
            self.rec(node.right, res)
