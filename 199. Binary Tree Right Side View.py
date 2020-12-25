'''
https://leetcode.com/problems/binary-tree-right-side-view/
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
'''
'''
DFS:  Retain a list of nodes in all levels.
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(node, path, depth):
            if node:
                if len(path) == depth:
                    path.append([])
                path[depth].append(node.val)
                helper(node.left, path, depth+1)
                helper(node.right, path, depth+1)
                
        path = []
        helper(root, path, 0)
        return list(a[-1] for a in path)
     
'''
BFS
Time:O(n)
Space:O(D) - D represents diameter of the tree.
'''
class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
        nextlevel = deque([root,])
        right = []
        
        while nextlevel:
            curr = nextlevel
            nextlevel = deque()
            while curr:
                node = curr.popleft()
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
            right.append(node.val)
            
        return right
