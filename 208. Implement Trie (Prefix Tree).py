'''
https://leetcode.com/problems/implement-trie-prefix-tree/
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. 
There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 
Example 1:
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]
'''
'''
Time:O(n)
Space:O(n)
'''
class TrieNode:
    def __init__(self, char = ''):
        self.char = char
        self.children = {}
        self.isEnd = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        root = self.root
        for ch in word:
            if ch in root.children:
                root = root.children[ch]
            else:
                newnode = TrieNode(ch)
                root.children[ch] = newnode
                root = newnode
        root.isEnd = True

    def search(self, word: str) -> bool:
        root = self.root
        for ch in word:
            if ch in root.children:
                root = root.children[ch]
            else:
                return False
        return root.isEnd

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for ch in prefix:
            if ch in root.children:
                root = root.children[ch]
            else:
                return False
        return True
