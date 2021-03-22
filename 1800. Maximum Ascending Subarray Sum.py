'''
https://leetcode.com/problems/maximum-ascending-subarray-sum/
Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.
A subarray is defined as a contiguous sequence of numbers in an array.
A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi < numsi+1. Note that a subarray of size 1 is ascending.

Example 1:

Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.

'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            if i==0 or nums[i-1] >= nums[i]:
                cur = 0
            cur += nums[i]
            res = max(cur, res)
        return res
