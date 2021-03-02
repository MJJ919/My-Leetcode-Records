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
Time:O(2**n)
Space:O(n)
'''
class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        def back(subset, start, nums, target):
            if target<0:    return 
            if target==0:   res.append(subset[:])
            for i in range(start, len(nums)):
                num, freq = nums[i]
                if freq>0:
                    subset.append(num)
                    nums[i] = (num, freq-1)
                    back(subset, i, nums, target-num)
                    nums[i] = (num, freq)
                    subset.pop()
            
        res = []
        nums = Counter(nums)
        nums = [(num, nums[num])for num in nums]
        print(nums)
        back([], 0, nums, target)
        return res

       
class Solution:
    def combinationSum2(self, c: List[int], target: int) -> List[List[int]]:
        c.sort()
        res = []
        def back(path, target, c):
            if target==0 and path not in res:                
                res.append(path[:])
                return 
            if target<0:
                return
            for i in range(len(c)):
                if i>0 and c[i]==c[i-1]:
                    continue
                path.append(c[i])
                back(path, target-c[i], c[i+1:])
                path.pop()
        back([], target, c)
        return res
