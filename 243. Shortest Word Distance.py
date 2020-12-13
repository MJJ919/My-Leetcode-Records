'''
https://leetcode.com/problems/shortest-word-distance/
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dis = a = b = float('inf')
        for i, ch in enumerate(words):
            if ch == word1:
                a = i
            if ch ==word2:
                b = i
            dis = min(dis, abs(a-b))
        return dis
