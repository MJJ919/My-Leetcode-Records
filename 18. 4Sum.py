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
        out, res = [], []
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                s = target-nums[i]-nums[j]
                m, n = j+1, len(nums)-1
                while m<n:
                    if nums[m]+nums[n]<s:
                        m += 1
                    elif nums[m]+nums[n]>s:
                        n -= 1
                    elif nums[m]+nums[n]==s:
                        out.append([nums[i],nums[j],nums[m],nums[n]])
                        m += 1
        for i in out:
            if i not in res:
                res.append(i)
        return res

    
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        seen = set()
        if not nums:    return res
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                comp = target-nums[i]-nums[j]
                lo, hi = j+1, len(nums)-1
                while lo<hi:
                    if nums[lo]+nums[hi]==comp:
                        l = sorted([nums[i], nums[j], nums[lo], nums[hi]])
                        if tuple(l) not in seen:
                            seen.add(tuple(l))
                            res.append([nums[i], nums[j], nums[lo], nums[hi]])
                        lo += 1
                        hi -= 1
                    elif nums[lo]+nums[hi]<comp:
                        lo += 1
                    else:
                        hi -= 1
        return res
