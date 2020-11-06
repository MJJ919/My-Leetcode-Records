'''
https://leetcode.com/problems/combination-sum-ii/
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[[1,1,6],[1,2,5],[1,7],[2,6]]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: [[1,2,2],[5]]
 
Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
'''

'''
Time:O()
Space:O()
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result=[]
        self.sum(candidates,0,[],result,target)
        return result
    
    def sum(self,nums,start,path,result,target):
        if not target:                 
            result.append(path)
        for i in xrange (start,len(nums)):
            if nums[i]>target:
                break   #Solution doesn't find. Break.
            if i> start and nums[i] == nums[i-1]:
                continue    #Avoid Duplicate.
            else:    
                self.sum(nums, i+1, path+[nums[i]], result, target-nums[i])
       
