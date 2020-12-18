'''
https://leetcode.com/problems/wiggle-sort/
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Example:
Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]
'''
'''
Time:O(nlgn)
Space:O(1)
'''
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        i, n = 1, len(nums)
        while i < n-1:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            i += 2
            
'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def wiggleSort(self, nums):
        for i in range(len(nums) - 1):
            if (i % 2 == 0 and nums[i] > nums[i + 1] ) or (i % 2 == 1 and nums[i] < nums[i + 1]):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
