'''
https://leetcode.com/problems/subsets-ii/
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

Example:
Input: [1,2,2]
Output:
[[2],[1],[1,2,2],[2,2],[1,2],[]]
'''
'''
Time:O(n*2^n)
Space:O(n*2^n)
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def back(subset, n):
            if subset not in res:
                res.append(subset[:])
            for i in range(n,len(nums)):
                subset.append(nums[i])
                back(subset, i+1)
                subset.pop()
            
        res = []
        nums.sort()
        back([], 0)
        return res
