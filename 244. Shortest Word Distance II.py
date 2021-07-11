'''
https://leetcode.com/problems/shortest-word-distance-ii/
Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and
return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters. 

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
'''
'''
Time:O(n)
Space:O(n)
'''
class WordDistance:

    def __init__(self, words: List[str]):
        self.d = defaultdict(list)
        for i, ch in enumerate(words):
            self.d[ch].append(i)
        
    def shortest(self, word1: str, word2: str) -> int:
        l1, l2 = self.d[word1], self.d[word2]
        i, j = 0, 0
        res = float('inf')
        while i<len(l1) and j<len(l2):
            res = min(res, abs(l1[i]-l2[j]))
            if l1[i]>l2[j]:
                j += 1
            else:
                i += 1
        return res
