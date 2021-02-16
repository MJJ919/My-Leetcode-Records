'''
https://leetcode.com/problems/binary-search-tree-iterator/
'''
'''
Use list to store nodes.
Time:O(n)
Space:O(n)
'''
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.traverse = []
        def helper(node):
            if node:
                helper(node.left)
                self.traverse.append(node.val)
                helper(node.right)
            return node
        helper(root)
        self.pointer = -1
    def next(self) -> int:
        self.pointer += 1
        return self.traverse[self.pointer]

    def hasNext(self) -> bool:
        return self.pointer+1<len(self.traverse)

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
