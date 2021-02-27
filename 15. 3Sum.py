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
Space:O(logn) to O(n)
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        if not nums:
            return res
        
        def find(i):
            lo, hi = i+1, len(nums)-1
            while lo<hi:
                s = nums[i]+nums[lo]+nums[hi]
                if s<0:
                    lo += 1 
                elif s>0:
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi], nums[i]])
                    lo, hi = lo+1, hi-1
                    while lo<hi and nums[lo-1]==nums[lo]:
                        lo += 1
                    
        for i in range(len(nums)-2):
            if nums[i]>0:
                break
            if i==0 or nums[i-1]!=nums[i]:
                find(i)
        return res
