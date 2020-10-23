'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
'''

'''
Method below convert int to str.
'''

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num>9:
            num = sum(int(c) for c in str(num))
        return num
        
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num>9:
            temp = 0
            while num>0:
                temp = temp + num%10
                num = num//10
            num = temp
        return num
