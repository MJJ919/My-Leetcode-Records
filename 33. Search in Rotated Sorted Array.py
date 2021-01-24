'''
https://leetcode.com/problems/search-in-rotated-sorted-array/
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
Formula: If a sorted array is shifted, if you take the middle, always one side will be sorted. Take the recursion according to that rule.

1- take the middle and compare with target, if matches return.
2- if middle is bigger than left side, it means left is sorted
2a- if [left] < target < [middle] then do recursion with left, middle - 1 (right)
2b- left side is sorted, but target not in here, search on right side middle + 1 (left), right
3- if middle is less than right side, it means right is sorted
3a- if [middle] < target < [right] then do recursion with middle + 1 (left), right
3b- right side is sorted, but target not in here, search on left side left, middle -1 (right)
'''
'''
Time:O(logn)
Space:O(1)
'''
class Solution:
    def search(self, nums: List[int], t: int) -> int:
        i, j = 0, len(nums)-1
        while i<=j:
            mid = (i+j)//2
            if nums[mid]==t:
                return mid
            elif nums[mid]>=nums[i]:
                if t>=nums[i] and t<nums[mid]:
                    j = mid-1
                else:
                    i = mid+1
            else:
                if nums[mid]<t and t<=nums[j]:
                    i = mid+1
                else:
                    j = mid-1
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
