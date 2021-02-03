'''
https://leetcode.com/problems/combination-sum/
Similar question: 40,216.
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
'''

'''
Time:
Space:
'''
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def back(subset, start, target):
            if target<0:
                return 
            elif target==0:
                res.append(subset[:])
            for i in range(start, len(nums)):
                subset.append(nums[i])
                back(subset, i, target-nums[i])
                subset.pop()
        
        res = []
        back([], 0, target)
        return res
