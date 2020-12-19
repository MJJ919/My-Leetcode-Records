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
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        self.reverse(s, 0, len(s)-1)
        self.re_word(s)
    
    def reverse(self, s, left, right):
        while left<right:
            s[left], s[right] = s[right], s[left]
            left, right = left+1, right-1
    
    def re_word(self, s):
        n = len(s)
        i = j = 0
        while i<n:
            while j<n and s[j]!=' ':
                j += 1
            self.reverse(s, i, j-1)
            i,j = j+1, j+1
