'''
https://leetcode.com/problems/design-search-autocomplete-system/
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.hot = 0
        
class AutocompleteSystem:
    def add(self, s, hot):
        node = self.root
        for ch in s:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True
        node.hot -= hot
        
    def __init__(self, sentences: List[str], times: List[int]):
        self.newinput = ''
        self.root =TrieNode()
        for idx, s in enumerate(sentences):
            self.add(s, times[idx])
    
    def search(self, newinput):
        res = []
        path = ''
        node = self.root
        for ch in newinput:
            if ch not in node.children:
                return res
            node = node.children[ch]
            path += ch
        self.dfs(node, path, res)
        return [l[1] for l in sorted(res)[:3]]
        
    def dfs(self, node, path, res):
        if node.isEnd:
            res.append([node.hot, path])
            
        for ch in node.children:
            self.dfs(node.children[ch], path+ch, res)
        
    def input(self, c: str) -> List[str]:
        if c != '#':
            self.newinput += c
            return self.search(self.newinput)
        else:
            self.add(self.newinput, 1)
            self.newinput = ''
