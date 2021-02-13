'''
https://leetcode.com/problems/range-sum-of-bst/
Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].
Example 1:
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def search(node):
            if not node:
                return
            if node.val<low:
                search(node.right)
            elif node.val>high:
                search(node.left)
            else:
                self.res += node.val
                search(node.left)
                search(node.right)
        self.res = 0
        search(root)        
        return self.res
