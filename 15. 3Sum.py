'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []
'''
'''
Method below uses twosum.
Time:O(n**2)
Space:O(logn) to log(n)
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i==0 or nums[i] != nums[i-1]:
                self.sum(nums, i, res)
        return res
        
    def sum(self, nums, i, res):
        seen = set()
        j = i+1            
        while j<len(nums):
            comp = -nums[i]-nums[j]
            if comp in seen:
                res.append([comp, nums[i], nums[j]])
                while j+1 < len(nums) and nums[j] == nums[j+1]:
                    j += 1
            seen.add(nums[j])
            j += 1
