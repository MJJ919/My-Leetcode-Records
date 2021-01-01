'''
https://leetcode.com/problems/powx-n/
Implement pow(x, n), which calculates x raised to the power n (i.e. xn).

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
        return pow(x,n)

'''
Recursion
Time:O(lgn)
Space:O(lgn)
'''
class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n<0:
            return 1/self.myPow(x,-n)
        if n%2:
            return x*self.myPow(x, n-1)
        return self.myPow(x*x, n/2)
 
'''
Iterative
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
