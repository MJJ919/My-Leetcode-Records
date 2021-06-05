'''
https://leetcode.com/problems/word-ladder/
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words such that:

The first word in the sequence is beginWord.
The last word in the sequence is endWord.
Only one letter is different between each adjacent pair of words in the sequence.
Every word in the sequence is in wordList.
Given two words, beginWord and endWord, and a dictionary wordList, 
return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
'''
'''
Bidirectional BFS
'''
class Solution:
    def ladderLength(self, begin: str, end: str, wordList: List[str]) -> int:
        if not begin or not end or not wordList or end not in wordList: return 0
        words = set(wordList)
        n = len(begin)
        visited = set()
        beginset, endset = deque(), deque()
        beginset.append(begin)
        endset.append(end)
        depth = 1
        while beginset:
            nextset = deque()
            for _ in range(len(beginset)):
                word = beginset.popleft()
                if word in endset:   return depth
                for i in range(n):
                    for j in range(97, 123):
                        new = word[:i]+chr(j)+word[i+1:]
                        if new in endset:
                            return depth+1
                        if new not in visited and new in words:
                            nextset.append(new)
                            visited.add(new)
            if len(endset)<len(nextset):
                beginset, endset = endset, nextset
            else:
                beginset = nextset
            depth += 1  
        return 0
 
'''
Traditional BFS
'''
class Solution:
    def ladderLength(self, begin: str, end: str, wordList: List[str]) -> int:
        if not begin or not end or not wordList or end not in wordList: return 0
        words = set(wordList)
        n = len(begin)
        q = deque()
        q.append(begin)
        depth = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word==end:   return depth
                for i in range(n):
                    for j in range(97, 123):
                        new = word[:i]+chr(j)+word[i+1:]
                        if new in words:
                            if new == end:
                                return depth+1
                            words.remove(new)
                            q.append(new)
            depth += 1  
        return 0
