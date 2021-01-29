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
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        d = {'6':'9', '0':'0', '8':'8', '9':'6','1':'1' }
        i, j = 0, len(num)-1
        while i<=j:
            if num[i] not in d or d[num[i]]!=num[j]:
                return False
            i, j = i+1, j-1
        return True
