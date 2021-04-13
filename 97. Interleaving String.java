/*
https://leetcode.com/problems/interleaving-string/
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
*/
/*
Time:O(m*n)
Space:O(1)
*/
class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        int l1 = s1.length();
        int l2 = s2.length();
        if (l1+l2 != s3.length())   return false;
        boolean[] dp = new boolean[l2+1];
        for (int i=0; i<l1+1; i++){
            for (int j=0; j<l2+1; j++){
                if(i==0 && j==0)    dp[j] = true;
                else if (i==0)  dp[j] = dp[j-1] && s2.charAt(j-1)==s3.charAt(i+j-1);
                else if (j==0)  dp[j] = dp[j] && s1.charAt(i-1)==s3.charAt(i+j-1);
                else    dp[j] = (dp[j-1] && s2.charAt(j-1)==s3.charAt(i+j-1)) || (dp[j] = dp[j] && s1.charAt(i-1)==s3.charAt(i+j-1));
            }
        }
        return dp[l2];
    }
}

/*
Time:O(m*n)
Space:O(m*n)
*/
class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        int l1 = s1.length();
        int l2 = s2.length();
        if (s3.length() != l1 + l2) return false;
        boolean[][] dp = new boolean[l1+1][l2+1];
        for (int i=0; i<l1+1; i++){
            for (int j=0; j<l2+1; j++){
                if (i==0 && j==0)   dp[i][j] = true;
                else if (i==0) dp[i][j] = dp[i][j-1] && s2.charAt(j-1)==s3.charAt(i+j-1);
                else if (j==0) dp[i][j] = dp[i-1][j] && s1.charAt(i-1)==s3.charAt(i+j-1);
                else{
                    dp[i][j] = (dp[i-1][j] && s1.charAt(i-1) == s3.charAt(i+j-1)) || (dp[i][j-1] && s2.charAt(j-1) == s3.charAt(i+j-1));
                }
            }
        }
        return dp[l1][l2];
    }
}
