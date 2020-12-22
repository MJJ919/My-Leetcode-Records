'''
https://leetcode.com/problems/palindrome-partitioning/
Given a string s, partition s such that every substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s.
A palindrome string is a string that reads the same backward as forward.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
'''
'''
Time:O(n* 2**n)
Space:O(n)
'''
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs(s, [], res)
        return res
    
    def ispal(self, s):
        return s == s[::-1]
    
    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s)+1):
            if self.ispal(s[:i]):
                self.dfs(s[i:], path + [s[:i]], res)
