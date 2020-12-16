'''
https://leetcode.com/problems/product-of-array-except-self/
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.
'''
'''
Time:O(n)
Spaec:O(n)
'''
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        l, r,product = [0]*n, [0]*n,[0]*n
        l[0], r[n-1] = 1, 1
        for i in range(1, n):
            l[i] = l[i-1]*nums[i-1]
        for i in reversed(range(n-1)):
            r[i] = r[i+1]*nums[i+1]
        for i in range(n):
            product[i] = l[i]*r[i]
        return product
 
'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def productExceptSelf(self, nums):
        product = [0]*len(nums)
        product[0] = 1
        for i in range(1, len(nums)):
            product[i] = product[i-1]*nums[i-1]
        r = 1
        for i in reversed(range(len(nums))):
            product[i] = product[i]*r
            r = r*nums[i]
        return product
