/*
https://leetcode.com/problems/longest-palindromic-subsequence/
Given a string s, find the longest palindromic subsequence's length in s.
A subsequence is a sequence that can be derived from another sequence 
by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
*/
/*
Time:O(n*n)
Space:O(n*n)
*/
class Solution {
    int[][] memo;
    public int longestPalindromeSubseq(String s) {
        int n = s.length();
        this.memo = new int[n][n];
        return find(0, n-1, s);
    }
    
    public int find(int i, int j, String s){
        if (i==j)   return 1;
        if (i>j)    return 0;
        if (memo[i][j]!=0)  return memo[i][j];
        if (s.charAt(i)==s.charAt(j))  memo[i][j] = 2+find(i+1, j-1, s);
        else    memo[i][j] = Math.max(find(i, j-1, s), find(i+1, j, s));
        return memo[i][j];
    }
}

/*
Time:O(n*n)
Space:O(n*n)
*/
class Solution {
    public int longestPalindromeSubseq(String s) {
        int n = s.length();
        int[][] dp = new int[n][n];
        for (int i=n-1; i>=0; i--){
            dp[i][i] = 1;
            for (int j=i+1; j<n; j++){
                if (s.charAt(i)==s.charAt(j))
                    dp[i][j] = 2+dp[i+1][j-1];
                else    dp[i][j] = Math.max(dp[i+1][j], dp[i][j-1]);
            }
        }
        return dp[0][n-1];
    }
}
