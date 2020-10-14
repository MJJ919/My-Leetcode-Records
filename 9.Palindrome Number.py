class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < -2**31 or x > 2**31-1:
            return false
        else:
            palindrome = str(x)[::-1]
        if palindrome == str(x):
            return True
