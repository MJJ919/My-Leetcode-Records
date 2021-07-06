'''
https://leetcode.com/problems/design-in-memory-file-system/
'''
'''
'''
class TrieNode():
    def __init__(self):
        self.children = {}
        self.content = ''
        self.isfile = False
        
class FileSystem:        
    def __init__(self):
        self.root = TrieNode()

    def add(self, path):
        node = self.root
        path = path.split('/')[1:]
        for word in path:
            if word not in node.children:
                node.children[word] = TrieNode()
            node = node.children[word]
        return node
    
    def ls(self, path: str) -> List[str]:
        if path=='/':
            return sorted(self.root.children.keys())
        node = self.add(path)
        if node.isfile:
            return path.split('/')[-1]
        return sorted(node.children.keys())
        
        
    def mkdir(self, path: str) -> None:
        self.add(path)
        
    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.add(filePath)
        node.content += content
        node.isfile = True

    def readContentFromFile(self, filePath: str) -> str:
        node = self.add(filePath)
        return node.content
