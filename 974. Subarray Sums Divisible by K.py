'''
https://leetcode.com/problems/subarray-sums-divisible-by-k/
Given an array nums of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by k.

Example 1:
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        res = 0
        prefix = 0
        for num in nums:
            prefix = (prefix+num%k+k)%k
            res += d[prefix]
            d[prefix] += 1
        return res
