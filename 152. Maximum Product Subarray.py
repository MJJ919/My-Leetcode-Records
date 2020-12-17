'''
https://leetcode.com/problems/maximum-product-subarray/
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''
'''
Time:O(n**2)
Space:O(1)
'''
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        res = nums[0]
        for i in range(len(nums)):
            acc = 1
            for j in range(i,len(nums)):
                acc = acc * nums[j]
                res = max(res, acc)
        return res
        
'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def maxProduct(self, nums):
        if len(nums) == 0:
            return 0
        mx, mn = nums[0], nums[0]
        res = mx
        for i in range(1, len(nums)):
            cur = nums[i]
            mx_tmp = max(cur, mx*cur, mn*cur)
            mn = min(cur, mx*cur, mn*cur)
            mx = mx_tmp
            res = max(res, mx)
        return res
