'''
https://leetcode.com/problems/strobogrammatic-number/
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:
Input: num = "69"
Output: true

Example 3:
Input: num = "962"
Output: false

Example 4:
Input: num = "1"
Output: true
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        d = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        i , j = 0, len(num)-1
        while i<=j:
            if num[i] not in d or num[j]!=d[num[i]]:    return False
            i, j = i+1, j-1
        return True
