'''
https://leetcode.com/problems/two-sum/
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''
'''
Method below uses hashtable.
Time:O(n)
Space:O(n)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        for i, ch in enumerate(nums):
            if target-ch not in d:
                d[ch] = i
            else:
                return [i, d[target-ch]]
            
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
