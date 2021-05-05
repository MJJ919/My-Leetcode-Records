/*
https://leetcode.com/problems/maximal-square/
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
*/
/*
Time:O(mn)
Space:O(n)
*/
class Solution {
    public int maximalSquare(char[][] matrix) {
        int rows = matrix.length, cols = rows>0? matrix[0].length:0;
        int[] dp = new int[cols+1];
        int max = 0, prev = 0;
        for(int i=1; i<rows+1; i++){
            for(int j=1; j<cols+1; j++){
                int temp = dp[j];
                if(matrix[i-1][j-1]=='1'){
                    dp[j] = Math.min(Math.min(dp[j-1], dp[j]), prev)+1;
                    max = Math.max(max, dp[j]);
                }
                else    dp[j]=0;
                prev = temp;
            }
        }
        return max*max;
    }
}

/*
Time:O(mn)
Space:O(mn)
*/
class Solution {
    public int maximalSquare(char[][] matrix) {
        int rows = matrix.length, cols = rows>0? matrix[0].length:0;
        int[][] dp = new int[rows+1][cols+1];
        int max = 0;
        for (int i=1; i<rows+1; i++){
            for (int j=1; j<cols+1; j++){
                if (matrix[i-1][j-1]=='1'){
                    dp[i][j] = Math.min(Math.min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1])+1;
                    max = Math.max(max, dp[i][j]);
                }
            }
        }
        return max*max;
    }
}
