'''
https://leetcode.com/problems/reverse-string/
Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''

'''
Time:O(n)
Spaec:O(1)
'''
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s.reverse()
        
'''
Time:O(lgn)
Space:O(1)
'''
class Solution(object):
    def reverseString(self, s):
        n = len(s)
        for i in range(n/2):
            s[i], s[n-i-1]=s[n-i-1],s[i]
        return s
