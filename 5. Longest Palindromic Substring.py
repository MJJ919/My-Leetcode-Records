'''
https://leetcode.com/problems/longest-palindromic-substring/
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a"
'''

'''
https://leetcode.com/problems/longest-palindromic-substring/discuss/2954/Python-easy-to-understand-solution-with-comments-(from-middle-to-two-ends)
Time:O(n**2)
Space:O(1)
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(s, left, right):
            while left>=0 and right<len(s):
                if s[left] == s[right]:
                    left, right = left-1, right+1
                else:
                    break
            return s[left+1:right]
        
        res  = ''
        for i in range(len(s)):
            res = max(helper(s, i, i), helper(s, i, i+1), res, key = len)
        return res
