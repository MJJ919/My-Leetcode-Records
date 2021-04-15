'''
Given an input string , reverse the string word by word. 

Example:
Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        
        def reverse(s, i, j):
            while i<=j:
                s[i], s[j] = s[j], s[i]
                i, j = i+1, j-1
        
        start, end = 0, 0 
        while start<len(s):
            while end<len(s) and s[end] != ' ':
                end += 1
            reverse(s, start, end-1)
            start, end = end+1, end+1

class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        i = 0
        j = 0
        while i<len(s):
            if s[i] == ' ':
                s[j:i] = s[j:i][::-1]
                j = i+1
            i += 1
        s[j:i] = s[j:i][::-1]
