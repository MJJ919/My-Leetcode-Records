'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''

'''
Method below uses hashtable.
Time:O(n)
Space:O(n)
'''

class Solution(object):
    def twoSum(self, nums, target):
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        compliments = {}
        for i, num in enumerate(nums):
            if target-num not in compliments:
                compliments[num] = i
            else:
                return [compliments[target-num], i]

'''
Method below uses brute force.
Time:O(n**2)
Space:O(1)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return [i, j]
