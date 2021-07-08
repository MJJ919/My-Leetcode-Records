'''
https://leetcode.com/problems/concatenated-words/
Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example 1:
Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
'''
'''
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True
            
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        for word in words:
            self.insert(word)
            
        def dfs(word, start, count, root):
            node = root
            for i in range(start, len(word)):
                if word[i] not in node.children:
                    return False
                node = node.children[word[i]]
                if node.isEnd:
                    if i==len(word)-1:
                        return count>=1
                    elif dfs(word, i+1, count+1, root):
                        return True
            return False
            
        
        res = []
        for word in words:
            if dfs(word, 0, 0, self.root):
                res.append(word)
        return res
