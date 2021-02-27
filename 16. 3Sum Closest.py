'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.
'''
'''
Time:O(n**2)
Space:O(1)
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        curmin = float('inf')
        res = 0
        nums.sort()
        for i in range(len(nums)-2):
            lo, hi = i+1, len(nums)-1
            while lo<hi:
                s = nums[i]+nums[lo]+nums[hi]
                if abs(s-target)<curmin:
                    curmin = abs(target-s)
                    res = s
                if s>target:
                    hi -= 1
                elif s<target:
                    lo += 1
                else:
                    return res
        return res
