'''
https://leetcode.com/problems/sqrtx/
Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
'''
'''
Method below uses 2 pointers.
Time:O(logN)
Space:O(1)
'''
class Solution(object):
    def mySqrt(self, x):
        if x<2:
            return x
        i,j = 0,x//2
        while i<=j:
            mid = (i+j)//2
            if mid*mid>x:
                j=mid-1
            elif mid*mid<x:
                i = mid+1
            else:
                return mid
        return j
'''
This way is pretty dumb.
'''


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 0
        while i*i < x:
            i += 1
        if i*i == x:
            return i
        else:
            return i-1
