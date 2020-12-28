'''
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. 
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:    return None
        nextlevel = deque([root])
        while nextlevel:
            size = len(nextlevel)
            for i in range(size):
                node = nextlevel.popleft()
                if i<size-1:
                    node.next = nextlevel[0]
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
        return root
        
'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def connect(self, root):
        if not root:    return root
        leftone = root
        while leftone.left:
            head = leftone
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftone = leftone.left
        return root
