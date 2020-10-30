'''
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
        if num<2:
            return True
        a, b = 2, num//2
        while a<=b:
            mid = a + (b-a)//2
            if mid*mid == num:
                return True
            if mid*mid < num:
                a = mid+1
            else:
                b = mid-1
        return False
