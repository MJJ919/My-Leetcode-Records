'''
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
Serialization is the process of converting a data structure or object into a 
sequence of bits so that it can be stored in a file or memory buffer, 
or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. 
There is no restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
'''
'''
Time:O(n)
Space:O(n)
'''
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:    return 'None'
        return str(root.val)+','+self.serialize(root.left)+','+self.serialize(root.right)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        s = data.split(',')
        def helper(s):
            num = s.pop(0)
            if num == 'None':
                return None
            root = TreeNode(num)
            root.left = helper(s)
            root.right = helper(s)
            return root
        return helper(s)
