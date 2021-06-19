/*
https://leetcode.com/problems/k-inverse-pairs-array/
For an integer array nums, an inverse pair is a pair of integers [i, j] 
where 0 <= i < j < nums.length and nums[i] > nums[j].

Given two integers n and k, return the number of different arrays consist of numbers 
from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 109 + 7.

Example 1:
Input: n = 3, k = 0
Output: 1
Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.
*/
/*
Time:O(n*n*k)
Space:O(n*k)
*/
public class Solution {
    public int kInversePairs(int n, int k) {
        int mod = (int)Math.pow(10, 9)+7;
        int[][] dp = new int[n + 1][k + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= k; j++) {
                if (j == 0)
                    dp[i][j] = 1;
                else {
                    for (int p = 0; p <= Math.min(j, i - 1); p++)
                        dp[i][j] = (dp[i][j] + dp[i - 1][j - p]) % mod;
                }
            }
        }
        return dp[n][k];
    }
}
