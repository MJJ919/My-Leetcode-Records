'''
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
'''
Method below convert int into str first then convert str back to int.
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
Method below uses math.
Time:O(log(x))
Space:O(1)
'''     
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = 0
        a = 1
        if x<0:
            a = -1
            x = -x
        while x>0:
            r = r*10 + x%10
            x = x//10
        return 0 if r > pow(2,31) else r*a
