'''
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
Follow up: Could you write an algorithm with O(log n) runtime complexity?

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
'''
'''
Time:O(lgn)
Space:O(1)
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums)-1
        p = -1
        while i<=j:
            mid = (i+j)//2
            if nums[mid]==target:
                p = mid
                break
            elif nums[mid]>target:
                j = mid-1
            else:
                i = mid+1
        if p==-1:   return [-1, -1]
        else:
            left = right = p
            while left>=0 and nums[left]==target:
                left -= 1
            while right<len(nums) and nums[right]==target:
                right += 1
        return [left+1, right-1]
    
'''
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = defaultdict(list)
        for i,ch in enumerate(nums):
            d[ch].append(i)
        res = []
        res.append(d.get(target,[-1,-1])[0])
        res.append(d.get(target,[-1,-1])[-1])
        return res
