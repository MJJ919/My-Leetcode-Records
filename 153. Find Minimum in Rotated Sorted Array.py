'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums, return the minimum element of this array.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
'''
'''
Time:O(nlgn)
Space:O(1)
'''
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return min(nums)
        
'''        
Time:O(lgn)
Space:O(1)
'''
class Solution(object):
    def findMin(self, nums):
        i, j = 0, len(nums)-1
        while i<j:
            mid = (i+j)//2
            if nums[mid]>nums[j]:
                i = mid+1
            else:
                j = mid
        return nums[j]

class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums)-1
        while i<=j:
            mid = (i+j)//2
            if nums[mid]>nums[-1]:
                i = mid+1
            elif mid == 0 or nums[mid]<nums[mid-1]:
                return nums[mid]
            else:
                j = mid-1
