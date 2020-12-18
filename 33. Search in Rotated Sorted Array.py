'''
You are given an integer array nums sorted in ascending order, and an integer target.
Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''

'''
Method below uses 2 pointers.
Time:O(logn)
Space:O(1)
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        a,b = 0, len(nums)-1
        while a<=b:
            mid = a+(b-a)//2
            if target == nums[mid]:
                return mid
            if nums[mid]>=nums[a]:
                if target<nums[mid] and target>=nums[a]:
                    b = mid-1
                else:
                    a = mid+1
            else:
                if target>nums[mid] and target<=nums[b]:
                    a = mid+1
                else:
                    b = mid-1
        return -1
                    
'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def search(self, nums, target):
        for i, ch in enumerate(nums):
            if target == ch:
                return i
        return -1
