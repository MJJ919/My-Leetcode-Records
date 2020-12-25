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
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        nextlevel = deque([root])
        order = []
        depth = 0
        
        while nextlevel:
            order.append([])
            curr = nextlevel
            nextlevel = deque()
            while curr:
                node = curr.popleft()
                order[depth].append(node.val)
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            if depth%2 == 1:
                order[depth] = order[depth][::-1]
            depth += 1
            
        return order
        
'''
DFS
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def zigzagLevelOrder(self, root):
        def helper(node, path, depth):
            if node:
                if len(path) == depth:
                    path.append(deque([]))
                if depth%2 == 0:
                    path[depth].append(node.val)
                else:
                    path[depth].appendleft(node.val)
                helper(node.left, path, depth+1)
                helper(node.right, path, depth+1)
        
        path = []
        helper(root, path, 0)
        return path
