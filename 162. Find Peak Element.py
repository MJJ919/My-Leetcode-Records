'''
https://leetcode.com/problems/find-peak-element/
A peak element is an element that is strictly greater than its neighbors.
Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
'''
'''
Time:O(lgn)
Space:O(1)
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i, j = 0, len(nums)-1
        while i<j:
            mid = (i+j)//2
            if nums[mid]>nums[mid+1]:
                j = mid
            else:
                i = mid+1
        return i
    
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                return i-1
        return len(nums)-1
