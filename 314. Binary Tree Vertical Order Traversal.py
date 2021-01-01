'''
https://leetcode.com/problems/binary-tree-vertical-order-traversal/
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).
If two nodes are in the same row and column, the order should be from left to right.

Examples 1:
Input: [3,9,20,null,null,15,7]

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7 

Output:

[
  [9],
  [3,15],
  [20],
  [7]
]
'''
'''
Time:O(nlgn)  #We use sorted() function here.
Space:O(n)
'''
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        d = defaultdict(list)
        q = deque([(root, 0)])
        while q:
            node, column = q.popleft()
            if node is not None:
                d[column].append(node.val)
                q.append((node.left, column-1))
                q.append((node.right, column+1))
        return [d[x] for x in sorted(d.keys())]
