'''
https://leetcode.com/problems/n-ary-tree-level-order-traversal/
Given an n-ary tree, return the level order traversal of its nodes' values.
Nary-Tree input serialization is represented in their level order traversal, 
each group of children is separated by the null value (See examples).

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root:
            return res
        nodes= deque()
        nodes.append(root)
        while nodes:
            length = len(nodes)
            layer = []
            for i in range(length):
                node = nodes.popleft()
                layer.append(node.val)
                for children in node.children:
                    nodes.append(children)
            res.append(layer)
        return res
