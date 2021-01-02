'''
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
'''
'''
Time:O(lgn)-O(n)
Space:O(1)
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        i, j = 0, len(nums)-1
        while i<=j:
            while i<j and nums[i]==nums[i+1]:
                i += 1
            while i<j and nums[j]==nums[j-1]:
                j -= 1
            mid = (i+j)/2
            if nums[mid] == target:
                return True
            if nums[mid]>=nums[i]:
                if nums[i]<=target<nums[mid]:
                    j = mid-1
                else:
                    i = mid+1
            else:
                if target>nums[mid] and target<=nums[j]:
                    i = mid+1
                else:
                    j = mid-1
        return False
