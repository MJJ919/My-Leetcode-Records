'''
https://leetcode.com/problems/first-missing-positive/
Given an unsorted integer array nums, find the smallest missing positive integer.
Follow up: Could you implement an algorithm that runs in O(n) time and uses constant extra space.?

Example 1:
Input: nums = [1,2,0]
Output: 3
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
            n = len(nums)
            if not 1 in nums:
                return 1
            if n==1:    return 2
            for i in range(n):
                if nums[i]<=0 or nums[i]>n:
                    nums[i]=1
            for i in range(n):
                a = abs(nums[i])
                if a==n:
                    nums[0] = -abs(nums[0])
                else:
                    nums[a] = -abs(nums[a])
            for i in range(1,n):
                if nums[i]>0:
                    return i
            if nums[0]>0:
                return n
            return n+1
