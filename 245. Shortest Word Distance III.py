'''
https://leetcode.com/problems/shortest-word-distance-iii/
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
word1 and word2 may be the same and they represent two individual words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
Input: word1 = “makes”, word2 = “coding”
Output: 1
Input: word1 = "makes", word2 = "makes"
Output: 3
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        d = defaultdict(list)
        for i,ch in enumerate(words):
            d[ch].append(i)
        dis = float("inf")
        if word1 == word2:
            l = d[word1]
            for i in range(len(l)-1):
                dis = min(dis, l[i+1]-l[i])
        else:
            l1, l2 = d[word1], d[word2]
            i, j = 0, 0
            while i<len(l1) and j<len(l2):
                dis = min(dis, abs(l1[i]-l2[j]))
                if l1[i]<l2[j]:
                    i += 1
                else:
                    j += 1
        return dis
