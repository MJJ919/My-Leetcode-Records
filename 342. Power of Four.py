'''
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
'''

'''
Method below uses brute force.
'''
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        while num % 4 == 0:
            num /= 4
        return num == 1
 
'''
Method below uses power.
'''
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        n = 0
        power = 1
        while n<=16:
            if num == power:
                return True
            else:
                power = power * 4
                n += 1
        return False

'''
Method below uses log function.
'''
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num>0 and log(num,4).is_integer()
            
