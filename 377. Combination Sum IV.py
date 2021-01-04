'''
https://leetcode.com/problems/combination-sum-iv/
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:
nums = [1, 2, 3]
target = 4
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
Therefore the output is 7.
'''
'''
Time:O(T⋅N)
Space:O(T)
'''
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @functools.lru_cache(maxsize = None)
        def count(remain):
            if remain==0:
                return 1
            res = 0
            for i in nums:
                if remain-i>=0:
                    res += count(remain-i)
                #else:
                    #break
            return res
        
        return count(target)
