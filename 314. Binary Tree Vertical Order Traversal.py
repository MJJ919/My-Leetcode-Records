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

'''
DFS
'''
 class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        def search(node, row, width):
            if node:
                nonlocal minwidth, maxwidth
                d[width].append((row,node.val))
                minwidth = min(minwidth, width)
                maxwidth = max(maxwidth, width)
                search(node.left, row+1, width-1)
                search(node.right, row+1, width+1)
                
        if not root:    return []
        d, res = defaultdict(list), []
        minwidth = maxwidth = 0
        search(root,0,0)
        for i in range(minwidth, maxwidth+1):
            d[i].sort(key=lambda x:x[0])
            col = [val for row,val in d[i]]
            res.append(col)
        return res
