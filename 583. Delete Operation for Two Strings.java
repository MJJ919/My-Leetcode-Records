/*
https://leetcode.com/problems/delete-operation-for-two-strings/
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.
In one step, you can delete exactly one character in either string.

Example 1:
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
*/
/*
Time:O(mn)
Space:O(mn)
*/
class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length();
        int n = word2.length();
        int[][] memo = new int[m+1][n+1];
        for (int i = 1; i<=m; i++){
            for (int j = 1; j<=n; j++){
                if (word1.charAt(i-1)==word2.charAt(j-1))   memo[i][j] = 1 + memo[i-1][j-1];
                else    memo[i][j] = Math.max(memo[i-1][j], memo[i][j-1]);
            }
        }
        return m+n-memo[m][n]*2;
    }
}


class Solution {
    public int check(String w1, String w2, int i, int j, int[][] memo){
        if (i<0 || j<0) return 0;
        if (memo[i][j]>0)   return memo[i][j];
        if (w1.charAt(i)==w2.charAt(j)) memo[i][j] = 1+check(w1, w2, i-1, j-1, memo);
        else    memo[i][j] = Math.max(check(w1, w2, i, j-1, memo), check(w1, w2, i-1, j, memo));
        return memo[i][j];        
    }
    
    public int minDistance(String word1, String word2) {
        int m = word1.length();
        int n = word2.length();
        int[][] memo= new int[m][n];
        return m+n-check(word1, word2, m-1, n-1, memo)*2;
    }
}
