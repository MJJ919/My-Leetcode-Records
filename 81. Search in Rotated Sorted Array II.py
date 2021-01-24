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
class Solution:
    def search(self, nums: List[int], t: int) -> bool:
        i, j = 0, len(nums)-1
        while i<=j:
            while i<j and nums[i+1]==nums[i]:
                i += 1
            while i<j and nums[j-1]==nums[j]:
                j -= 1
            mid = (i+j)//2
            if nums[mid]==t:
                return True
            elif nums[mid]>=nums[i]:
                if t>=nums[i] and t<nums[mid]:
                    j = mid-1
                else:
                    i = mid+1
            else:
                if nums[mid]<t and nums[j]>=t:
                    i = mid+1
                else:
                    j = mid-1
        return False
