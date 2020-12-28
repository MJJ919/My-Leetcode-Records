'''
https://leetcode.com/problems/binary-search-tree-iterator/
'''
'''
Use list to store nodes.
Time:O(n)
Space:O(n)
'''
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.s = []
        self.index = -1
        self.inorder(root)
    
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            self.s.append(node.val)
            self.inorder(node.right)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        self.index += 1
        return self.s[self.index]
            

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.index < len(self.s)-1
        
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

'''
Iteration:
'''
def __init__(self, root):
        self.res, s = [], []
        self.index = -1
        
        while True:
            while root:
                s.append(root)
                root = root.left
            if not s:
                break
            node = s.pop()
            self.res.append(node.val)
            root = node.right
