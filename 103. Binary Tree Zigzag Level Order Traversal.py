'''
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''
'''
BFS
Time:O(n)
Space:O(n)
'''
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        level = 0
        nextlevel = deque([root])
        res = []
        
        while nextlevel:
            res.append([])
            cur = nextlevel
            nextlevel = deque()
            while cur:
                node = cur.popleft()
                res[level].append(node.val)
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            if level%2==1:
                res[level] = res[level][::-1]
            level += 1
            
        return res
        
'''
DFS
Time:O(n)
Space:O(n)
'''
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        def traverse(node, level):
            if node:
                if len(res)<=level:
                    res.append(deque())
                if level%2==1:
                    res[level].appendleft(node.val)
                else:
                    res[level].append(node.val)
                traverse(node.left, level+1)
                traverse(node.right, level+1)
        
        res = []
        traverse(root, 0)
        return res
