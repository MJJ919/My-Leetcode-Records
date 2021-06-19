'''
https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.
Recall that:
The node of a binary tree is a leaf if and only if it has no children
The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.
Note: This question is the same as 865: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest leaf-nodes of the tree.
Note that nodes 6, 0, and 8 are also leaf nodes, but the depth of them is 2, but the depth of nodes 7 and 4 is 3.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def dfs(node, level):
            if node:
                if len(d)<=level:
                    d.append([])
                d[level].append(node.val)
                dfs(node.left, level+1)
                dfs(node.right, level+1)
                
        def lca(node):
            if not node:
                return None
            if node.val in s:
                return node
            left = lca(node.left)
            right = lca(node.right)
            if left and right:
                return node
            if left:
                return left
            if right:
                return right
            return None
        
        d = []
        dfs(root, 0)
        s = set(d[-1])
        return lca(root)
    
    
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def traverse(node, level):
            if not node:
                return [None, level]
            left = traverse(node.left, level+1)
            right = traverse(node.right, level+1)
            if left[1]==right[1]:
                return [node, left[1]]
            elif left[1]<right[1]:
                return right
            else:
                return left
            
        return traverse(root, 0)[0]
