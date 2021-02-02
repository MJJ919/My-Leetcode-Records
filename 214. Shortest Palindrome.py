'''
https://leetcode.com/problems/shortest-palindrome/
Given a string s, you can convert it to a palindrome by adding characters in front of it. 
Find and return the shortest palindrome you can find by performing this transformation.

Example 1:
Input: s = "aacecaaa"
Output: "aaacecaaa"
'''
'''
'''
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        i = len(s)
        while not s[:i] == s[:i][::-1]:
            i -= 1
        return s[i:][::-1] + s 
