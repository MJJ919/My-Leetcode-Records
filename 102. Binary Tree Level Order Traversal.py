'''
https://leetcode.com/problems/binary-tree-level-order-traversal/
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        def traverse(node, level):
            if not node:    return
            if len(res)<=level:
                res.append([])
            res[level].append(node.val)
            traverse(node.left, level+1)
            traverse(node.right, level+1)
        traverse(root, 0)
        return res

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        d = defaultdict(list)
        def level(node, depth):
            if node:
                d[depth].append(node.val)
                level(node.left, depth+1)
                level(node.right, depth+1)
        level(root, 0)
        for depth, num in d.items():
            res.append(num)
        return res
