'''
https://leetcode.com/problems/move-zeroes/
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
'''
'''
Time:O(n) #Count() uses O(n).
Space:O(1)
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a = nums.count(0)
        for i in range(a):
            nums.remove(0)
            nums.append(0)
            
'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def moveZeroes(self, nums):
        z = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[z], nums[i] = nums[i], nums[z]
                z += 1
