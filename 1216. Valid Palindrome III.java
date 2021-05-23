/*
516变体
https://leetcode.com/problems/valid-palindrome-iii/
Given a string s and an integer k, return true if s is a k-palindrome.
A string is k-palindrome if it can be transformed into a palindrome by removing at most k characters from it.

Example 1:
Input: s = "abcdeca", k = 2
Output: true
Explanation: Remove 'b' and 'e' characters.
*/
/*
Time:O(n*n)
Space:O(n*n)
*/
class Solution {
    public boolean isValidPalindrome(String s, int k) {
        int n = s.length();
        int[][] dp = new int[n][n]; 
        for (int i=n-1; i>=0; i--){
            dp[i][i] = 1;
            for (int j=i+1; j<n; j++){
                if(s.charAt(i)==s.charAt(j))    dp[i][j] = 2+dp[i+1][j-1];
                else    dp[i][j] = Math.max(dp[i+1][j], dp[i][j-1]);
            }
        }
        return n-dp[0][n-1]<=k? true:false;
    }
}
