'''
https://leetcode.com/problems/subarray-sum-equals-k/
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        s = 0
        d = defaultdict(int)
        d[0] = 1
        for i in range(len(nums)):
            s += nums[i]
            if s-k in d:
                res += d[s-k]
            d[s] += 1
        return res
