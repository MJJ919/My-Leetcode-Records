'''
https://leetcode.com/problems/sum-of-two-integers/
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:
Input: a = 1, b = 2
Output: 3
'''
'''
Bit munipulation.
Time:O(1)
Space:O(1)
'''
class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y =abs(a), abs(b)
        if x<y:
            return self.getSum(b,a)
        sign = 1 if a>0 else -1
        if a*b>0:
            while y:
                x, y = x^y, (x&y)<<1
        else:
            while y:
                x, y = x^y, (~x&y)<<1
        return x*sign
