class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < -2**31 or x > 2**31-1:
            return False
        else:
            palindrome = str(x)[::-1]
        if palindrome == str(x):
            return True
       
'''
Method below does not convert int to str
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a = x
        if x < 0:
            return False
        else:
            reverse = 0
            while x > 0:
                reverse = x%10 + reverse*10
                x = x//10
        return reverse == a

