'''
https://leetcode.com/problems/binary-tree-paths/
Given a binary tree, return all root-to-leaf paths.
Note: A leaf is a node with no children.

Example:
Input:

   1
 /   \
2     3
 \
  5
Output: ["1->2->5", "1->3"]
'''
'''
Time:O(N)
Space:O(N)
'''
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def build(node, leaf):
            if not node:    return
            leaf += str(node.val)
            if not node.left and not node.right:
                res.append(leaf)
            leaf += '->'
            build(node.left, leaf)
            build(node.right, leaf)
        res = []
        build(root, '')
        return res
