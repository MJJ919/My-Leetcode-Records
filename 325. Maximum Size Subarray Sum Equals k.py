'''
https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:
Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4 
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        d = defaultdict()
        res = 0
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if s not in d:
                d[s] = i
                
            if s==k:
                res = max(res, i+1)
            elif s-k in d:
                res = max(res,i-d[s-k])
        return res
