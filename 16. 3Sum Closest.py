'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.
'''
'''
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
        m = float('inf')
        nums.sort()
        for n in range(len(nums)):
            i, j = n+1, len(nums)-1
            while i<j:
                s = nums[n]+nums[i]+nums[j]
                if abs(target-s)<abs(m):
                    m = target - s
                if s>target:
                    j -= 1
                else:
                    i += 1
            if m == 0:
                break
        return target - m
