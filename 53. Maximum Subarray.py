'''
https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [0]
Output: 0
'''

'''
Method below uses dynamic programming.
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = nums[0]
        for i in range(1,len(nums)):
            if nums[i-1]>0:
                nums[i] = nums[i]+nums[i-1]
            mx = max(nums[i],mx)
        return mx
