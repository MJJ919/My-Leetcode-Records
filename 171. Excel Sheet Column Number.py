'''
https://leetcode.com/problems/excel-sheet-column-number/
Given a column title as appear in an Excel sheet, return its corresponding column number.
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i,ch in enumerate(s):
            res += 26**(len(s)-i-1)*(ord(ch)-64)
        return res
        
        
class Solution(object):
    def titleToNumber(self, s):
        a = 0
        for i, ch in enumerate(s):
            a = a*26+ord(ch)-64
        return a
