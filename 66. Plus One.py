'''
https://leetcode.com/problems/plus-one
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
'''

'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        for i in range(len(digits)):
            a = len(digits)-i-1
            if digits[a] == 9:
                digits[a] = 0
            else:
                digits[a] += 1
                return digits
        return [1]+digits

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = ''.join(str(i) for i in digits)
        num = int(i)+1
        res = [int(x) for x in str(num)]
        if len(res)<len(digits):
            for i in range(0,len(digits)-len(res)):
                res.insert(0,0)
        return res
