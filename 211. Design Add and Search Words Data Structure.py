'''
https://leetcode.com/problems/design-add-and-search-words-data-structure/
Design a data structure that supports adding new words and finding if a string matches any previously added string.
Implement the WordDictionary class:
WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. 
word may contain dots '.' where dots can be matched with any letter.
'''
'''
Time:O(n)
Space:O(n)
'''
class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for ch in word:
            if not ch in node:
                node[ch] = {}
            node = node[ch]
        node['$'] = True
        
    def search(self, word: str) -> bool:
        def searchinnode(word, node):
            for i, ch in enumerate(word):
                if not ch in node:
                    if ch=='.':
                        for x in node:
                            if x != '$' and searchinnode(word[i+1:], node[x]):   return True
                    return False
                else:
                    node = node[ch]
            return '$' in node
        return searchinnode(word, self.trie)
        
        
class WordDictionary:
    def __init__(self):
        self.d = defaultdict(set)

    def addWord(self, word: str) -> None:
        self.d[len(word)].add(word)

    def search(self, word: str) -> bool:
        for w in self.d[len(word)]:
            for i in range(len(word)):
                if w[i]==word[i] or word[i]=='.':
                    if i==len(word)-1:
                        return True
                    else:
                        continue
                else:
                    break
        return False
        
