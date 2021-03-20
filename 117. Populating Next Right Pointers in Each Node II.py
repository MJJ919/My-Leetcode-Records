'''
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Example 1:
Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, 
just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q = deque([root])
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i<size-1:
                    node.next = q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
    
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def build(node, pre, leftmost):
            if node:
                if pre:
                    pre.next = node
                else:
                    leftmost = node
                pre = node
            return pre, leftmost
        
        if not root:
            return root
        leftmost = root
        while leftmost:
            pre, cur = None, leftmost
            leftmost = None
            while cur:
                pre, leftmost = build(cur.left, pre, leftmost)
                pre, leftmost = build(cur.right, pre, leftmost)
                cur = cur.next
        return root
