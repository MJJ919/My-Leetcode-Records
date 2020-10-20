'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

'''

'''
Method below scans string from right to left.
'''
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = 0
        for i, ch in enumerate(s[::-1]):
            a += (ord(ch)-64)*(26**i)
        return a
        
'''
Method below scans string from left to right.
'''
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = 0
        for i, ch in enumerate(s):
            a = a*26+ord(ch)-64
        return a
