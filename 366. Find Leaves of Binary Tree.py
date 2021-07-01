'''
Given the root of a binary tree, collect a tree's nodes as if you were doing this:
Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.
 
Example 1:
Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        res = []
        def dfs(node):
            if not node:
                return -1
            level = max(dfs(node.left), dfs(node.right))+1
            if len(res)<=level:
                res.append([])
            res[level].append(node.val)
            return level
        
        dfs(root)
        return res
