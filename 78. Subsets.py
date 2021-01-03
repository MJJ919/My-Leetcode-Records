'''
https://leetcode.com/problems/subsets/
Given an integer array nums, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. 

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
'''
'''
Cascading.
Time:O(n*2^n)
Space:O(n*2^n)
'''
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output=[[]]
        for i in nums:
            output = output+[cur + [i] for cur in output]
        return output

'''
Backtracking.
Time:O(n*2^n)
Space:O(n*2^n)
'''
class Solution(object):
    def subsets(self, nums):
        def back(start, cur):
            res.append(cur[:])
            
            for j in range(start, n):
                cur.append(nums[j])
                back(j+1,cur)
                cur.pop()
                
        res = []
        n = len(nums)
        back(0,[])
        return res
