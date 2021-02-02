'''
https://leetcode.com/problems/palindrome-number/
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
Follow up: Could you solve it without converting the integer to a string?
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: return False
        return str(x)==str(x)[::-1]

'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        s = str(x)
        for i,ch in enumerate(s):
            if ch != s[len(s)-i-1]:
                return False
        return True
       
'''
Method below does not convert int to str
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def isPalindrome(self, x):
        a = x
        if x < 0:
            return False
        else:
            reverse = 0
            while x > 0:
                reverse = x%10 + reverse*10
                x = x//10
        return reverse == a
