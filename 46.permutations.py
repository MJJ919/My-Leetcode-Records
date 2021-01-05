'''
https://leetcode.com/problems/permutations/
Given a collection of distinct integers, return all possible permutations.

Example:
Input: [1,2,3]
Output:
[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''
'''
backtracking.
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def back(cur):
            if len(cur)==n:
                res.append(cur[:])
            for i in nums:
                if i not in cur:
                    cur.append(i)
                    back(cur)
                    cur.pop()
        res, n = [], len(nums)
        back([])
        return res

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output=[]
        def back(first=0):
            if n==first:
                output.append(nums[:])
            for i in range(first,n):
                nums[i], nums[first] = nums[first], nums[i]
                back(first+1)
                nums[i], nums[first] = nums[first], nums[i]
        n = len(nums)
        back()
        return output
