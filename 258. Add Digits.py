'''
https://leetcode.com/problems/add-digits/
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:
Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
'''
'''
Math!
Time:O(1)
Space:O(1)
'''
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:    return 0
        return 9 if num%9 == 0 else num%9

'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def addDigits(self, num):
        while num >9:
            num = num%10 + num//10
        return num
