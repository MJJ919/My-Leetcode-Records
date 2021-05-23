/*
https://leetcode.com/problems/burst-balloons/
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. 
You are asked to burst all the balloons.
If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. 
If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.
Return the maximum coins you can collect by bursting the balloons wisely.
*/
/*
Time:O(n**3)
Space:O(n**2)
*/
class Solution {
    public int maxCoins(int[] nums) {
        int n = nums.length+2;
        int[] b = new int[n];
        b[0] = 1;
        b[n-1] = 1;
        for (int i=0; i<n-2; i++)   b[i+1] = nums[i];
        int[][] dp = new int[n][n];
        for (int i=n-2; i>=0; i--){
            for (int j=i+2; j<n; j++){
                for (int k=i+1; k<j; k++)
                    dp[i][j] = Math.max(dp[i][j], dp[i][k]+dp[k][j]+b[i]*b[k]*b[j]);
            }
        }
        return dp[0][n-1];
    }
}

class Solution {
    int[] b;
    public int maxCoins(int[] nums) {
        int n = nums.length+2;
        this.b = new int[n];
        this.b[0] = 1;
        this.b[n-1] = 1;
        for (int i=0; i<n-2; i++)   this.b[i+1] = nums[i];
        int[][] memo = new int[n][n];
        return burst(0, n-1, memo);
    }
    
    public int burst(int i, int j, int[][] memo){
        if (j<i)  return 0;
        if (memo[i][j]!=0)   return memo[i][j];
        for (int k=i+1; k<j; k++)
            memo[i][j] = Math.max(burst(i, k, memo)+burst(k, j, memo)+this.b[i]*this.b[k]*this.b[j], memo[i][j]);
        return memo[i][j];
    }
}
