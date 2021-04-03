'''
https://leetcode.com/problems/determine-color-of-a-chessboard-square/
'''
'''
Time:O(1)
Space:O(1)
'''
class Solution:
    def squareIsWhite(self, c: str) -> bool:
        return True if (ord(c[0])+int(c[1]))%2 else False
