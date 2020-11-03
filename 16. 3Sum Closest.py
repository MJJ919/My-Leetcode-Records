'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.
'''

'''
Method below uses 2 pointers.
Time:O(n**2)
Space:O(1)
'''
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        diff = float('inf')
        nums = sorted(nums)
        for i, ch in enumerate(nums):
            a,b = i+1, len(nums)-1
            while a<b:
                sum = ch+nums[a]+nums[b]
                if abs(sum-target)<abs(diff):
                    diff = target - sum
                if sum<target:
                    a = a+1
                else:
                    b = b-1
                if diff==0:
                    break
        return target - diff
