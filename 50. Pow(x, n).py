'''
https://leetcode.com/problems/powx-n/
Implement pow(x, n), which calculates x raised to the power n (i.e. xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
'''

'''
Method below uses python buildin function POW().
'''
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return pow(x,n)

'''
Method below uses iterative.
Time:O(logN)
Space:O(1)
'''
class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1.0
        if n<0:
            n = -n
            x = 1/x
        pow = 1
        while n:
            if n%2 == 1:
                pow = pow*x
            x = x*x
            n = n//2
        return pow
