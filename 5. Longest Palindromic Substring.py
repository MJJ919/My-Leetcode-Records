'''
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a"
'''

'''
Time:O(n**2)
Space:O(1)
https://leetcode.com/problems/longest-palindromic-substring/discuss/2954/Python-easy-to-understand-solution-with-comments-(from-middle-to-two-ends)
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        m = ''
        for i in xrange(len(s)):
            a = self.helper(s,i,i)
            if len(m)<len(a):
                m = a           # Or: m=max(m,a,key=len)
            a = self.helper(s,i,i+1)
            if len(m)<len(a):
                m = a
        return m
            
            
    def helper(self, s, l, r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l,r=l-1,r+1
        return s[l+1:r]
