/*
https://leetcode.com/problems/distinct-subsequences/
Given two strings s and t, return the number of distinct subsequences of s which equals t.
A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters 
without disturbing the relative positions of the remaining characters. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).
It's guaranteed the answer fits on a 32-bit signed integer.

Example 1:
Input: s = "rabbbit", t = "rabbit"
Output: 3
*/
/*
Time:O(M×N)
Space:O(M×N)
*/
class Solution {
    public int numDistinct(String s, String t) {
        int m = s.length();
        int n = t.length();
        int[][] dp = new int[m+1][n+1];
        for(int i=0; i<=m; i++)  dp[i][0] = 1;
        for (int i=1; i<=m; i++){
            for (int j=1; j<=n; j++){
                if (s.charAt(i-1)==t.charAt(j-1))
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
                else    dp[i][j] = dp[i-1][j];
            }
        }
        return dp[m][n];
    }
}
