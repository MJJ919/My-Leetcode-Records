'''
https://leetcode.com/problems/search-insert-position/
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
'''

'''
Time:O(logn)
Space:O(1)
'''
class Solution:
    def searchInsert(self, nums, target):
        if target<nums[0]:
            return 0
        if target>nums[-1]:
            return len(nums)
        left, right = 0, len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            elif target>nums[mid]:
                left = mid+1
            else:
                right = mid-1
        return left

'''
My method is a little bit awkward.
'''
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        else:
            for i in range(len(nums)):
                if target > nums[i]:
                    i += 1
                elif target <= nums[i]:
                    return i
