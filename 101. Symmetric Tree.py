'''
https://leetcode.com/problems/symmetric-tree/
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def symmetric(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return node1.val==node2.val and symmetric(node1.left, node2.right) and symmetric(node1.right, node2.left)
        
        return symmetric(root, root)
