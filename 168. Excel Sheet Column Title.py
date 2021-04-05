'''
https://leetcode.com/problems/excel-sheet-column-title/
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''
        while n!=0:
            n = n-1
            res += chr(n%26 + 65)
            n = n//26
        return res[::-1]
