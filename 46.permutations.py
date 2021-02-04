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
        def back(subset):
            if len(subset)==len(nums):
                res.append(subset[:])
            for num in nums:
                if num not in subset:
                    subset.append(num)
                    back(subset)
                    subset.pop()

        res = []
        back([])
        return res

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def back(start):
            if start==len(nums):
                res.append(nums[:])
            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                back(start+1)
                nums[i], nums[start] = nums[start], nums[i]

        res = []
        back(0)
        return res
