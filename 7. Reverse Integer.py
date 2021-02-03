'''
https://leetcode.com/problems/reverse-integer/
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
'''
Time:O(x)
Space:O(1)
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            reverse = int("-"+str(-x)[::-1])    
        else:
            reverse = int(str(x)[::-1])
        if reverse < -2**31 or reverse > 2**31-1:
            return 0
        else:
            return reverse
'''
Time:O(log(x))
Space:O(1)
'''     
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0: 
            x = -x
            flag = -1
        else:   flag = 1
        res = 0
        while x>0:
            res = res*10 + x%10
            x = x//10
        return 0 if res>pow(2,31) else res*flag
