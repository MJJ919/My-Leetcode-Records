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
class Solution:
    def ladderLength(self, begin: str, end: str, wordList: List[str]) -> int:
        if not begin or not end or not wordList or end not in wordList: return 0
        length = len(begin)
        word_mut = defaultdict(list)
        for word in wordList:
            for i in range(length):
                word_mut[word[:i]+'*'+word[i+1:]].append(word)
        q = deque([(begin, 1)])
        visited = {begin:True}
        while q:
            print(q)
            cur, count = q.popleft()
            for i in range(length):
                intermediate = cur[:i]+'*'+cur[i+1:]
                for word in word_mut[intermediate]:
                    if word == end:
                        return count+1
                    if word not in visited:
                        visited[word]=True
                        q.append((word, count+1))
                word_mut[intermediate] = []
        return 0
                    
