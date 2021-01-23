'''
https://leetcode.com/problems/wiggle-sort-ii/
Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
You may assume the input array always has a valid answer.

Example 1:
Input: nums = [1,5,1,1,6,4]
Output: [1,6,1,5,1,4]
Explanation: [1,4,1,5,1,6] is also accepted.
'''
'''
'''
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)
        mid = n//2 if len(nums)%2==0 else n//2+1
        first, second = nums[:mid], nums[mid:]
        first.reverse(), second.reverse()
        i = 0
        while i<n:
            if i%2 == 0:
                nums[i] = first[0]
                first = first[1:]
            else:
                nums[i] = second[0]
                second = second[1:]
            i += 1
