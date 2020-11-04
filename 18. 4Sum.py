'''
https://leetcode.com/problems/4sum/
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [], target = 0
Output: []
'''

'''
Time:O(n**3)
Space:O(1)
'''

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        output=[]
        result=[]
        nums=sorted(nums)
        if len(nums)<4:
            return output
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                p1,p2 = j+1,len(nums)-1
                while p1<p2:
                    if nums[p1]+nums[p2]<target - nums[i] - nums[j]:
                        p1 = p1+1
                    elif nums[p1]+nums[p2]>target - nums[i] - nums[j]:
                        p2 = p2-1
                    else:
                        output.append([nums[i], nums[j], nums[p1], nums[p2]])
                        p2 = p2-1
        for i in output:
            if i not in result:
                result.append(i)
        return result
