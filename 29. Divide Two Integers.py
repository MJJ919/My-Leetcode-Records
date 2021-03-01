'''
https://leetcode.com/problems/divide-two-integers/
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. 
For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For this problem, assume that your function returns 231 − 1 when the division result overflows.
 
Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
'''
'''
Time:O(logn**2)
Space:O(1)
'''
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        maxint = 2**31-1
        minint = -2**31
        halfmin = minint//2
        if dividend==minint and divisor==-1:
            return maxint
        negative = 2
        if dividend>0:
            negative -= 1
            dividend = -dividend
        if divisor>0:
            negative -= 1
            divisor = -divisor
        
        q = 0
        while divisor>=dividend:
            power = -1
            value = divisor
            while value>=halfmin and value+value>=dividend:
                value += value
                power += power
            q += power
            dividend -= value
        return -q if negative!=1 else q
