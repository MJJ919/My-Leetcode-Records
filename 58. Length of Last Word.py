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
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n, l = 0, len(s)
        while l>0:
            l -= 1
            if s[l]!=' ':
                n += 1
            elif n>0:
                return n
        return n
  
'''
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def lengthOfLastWord(self, s):
        return 0 if not s or s.isspace() else len(s.split()[-1])
