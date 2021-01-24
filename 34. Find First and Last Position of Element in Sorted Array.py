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
        def find(nums, target):
            i, j = 0, len(nums)-1
            while i<j:
                mid = (i+j)//2
                if nums[mid]<target:
                    i = mid+1
                elif nums[mid]>target:
                    j = mid
                else:
                    return mid
            return i
        
        if not nums:    return [-1,-1]
        idx = find(nums, target)
        if nums[idx]!=target:
            return [-1,-1]
        else:
            a, b = idx, idx
            while a>0 and nums[a-1]==target:
                a -= 1
            while b<len(nums)-1 and nums[b+1]==target:
                    b += 1
        return [a,b]
    
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
