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
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def back(start, cur):
            if cur not in res:
                res.append(cur[:])
            
            for i in range(start, n):
                cur.append(nums[i])
                back(i+1, cur)
                cur.pop()
                
        nums.sort()
        n, res = len(nums), []
        back(0, [])
        return res
