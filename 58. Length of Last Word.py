'''
https://leetcode.com/problems/length-of-last-word/
Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.
A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5

Example 2:
Input: s = " "
Output: 0
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = 0
        i = len(s)-1
        while i>=0:
            if s[i]!=' ':
                n += 1
            elif n>0:
                return n
            i -= 1
        return n
  
'''
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def lengthOfLastWord(self, s):
        return 0 if not s or s.isspace() else len(s.split()[-1])
