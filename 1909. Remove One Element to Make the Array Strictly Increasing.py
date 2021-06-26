'''
https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/
Given a 0-indexed integer array nums, return true if it can be made strictly increasing after removing exactly one element, 
or false otherwise. If the array is already strictly increasing, return true.
The array nums is strictly increasing if nums[i - 1] < nums[i] for each index (1 <= i < nums.length).

Example 1:
Input: nums = [1,2,10,5,7]
Output: true
Explanation: By removing 10 at index 2 from nums, it becomes [1,2,5,7].
[1,2,5,7] is strictly increasing, so return true.
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        idx = -1
        count = 0
        for i in range(len(nums)-1):
            if nums[i]>=nums[i+1]:
                idx = i
                count += 1
        
        if count==0:    return True
        if count>1: return False
        if count==1:
            if idx==0 or idx==len(nums)-2:
                return True
            if nums[idx-1]<nums[idx+1] or nums[idx]<nums[idx+2]:
                return True
