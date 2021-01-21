'''
https://leetcode.com/problems/minimum-size-subarray-sum/
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. 
If there isn't one, return 0 instead.

Example: 
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left = 0
        subsum = 0
        length = float('inf')
        for i in range(0,len(nums)):
            if subsum<s:
                subsum += nums[i]
            while (subsum>=s and left<=i):
                length = min(length, i-left+1)
                subsum -= nums[left]
                left += 1
        return length if length!=float('inf') else 0
