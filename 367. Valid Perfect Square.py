'''
https://leetcode.com/problems/valid-perfect-square/
Given a positive integer num, write a function which returns True if num is a perfect square else False.
Follow up: Do not use any built-in library function such as sqrt.
'''

'''
Method below uses binary search.
Time: O(logN)
Space: O(1)
'''
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2: return True
        i, j = 1, num/2
        while i<=j:
            mid = (i+j)/2
            sqr = mid*mid
            if sqr == num:
                return True
            elif sqr > num:
                j = mid-1
            else:
                i = mid+1
        return False
