'''
https://leetcode.com/problems/maximum-length-of-repeated-subarray/
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

Example 1:
Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].
'''
'''
Time:O(mn)
Space:O(mn)
'''
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0 for _ in range(n)]for _ in range(m)]
        res = float('-inf')
        for i in range(m):
            for j in range(n):
                if nums1[i]==nums2[j]:
                    if i==0 or j==0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1]+1
                res = max(res, dp[i][j])
        return res
                    
