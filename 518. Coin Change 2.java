/*
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
You may assume that you have an infinite number of each kind of coin.
The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
*/
/*
Time:O(mn)
Space:O(m)
*/
class Solution {
    public int change(int amount, int[] coins) {
        int[] pre = new int[amount+1];
        pre[0] = 1;
        for (int i=1; i<=coins.length; i++){
            int coin = coins[i-1];
            int[] cur = new int[amount+1];
            cur[0] = 1;
            for (int j=1; j<=amount; j++){
                if (j<coin) cur[j] = pre[j];
                else    cur[j] = pre[j] + cur[j-coin];
            }
            pre = cur;
        }
        return pre[amount];
    }
}

/*
Time:O(mn)
Space:O(mn)
*/
class Solution {
    public int change(int amount, int[] coins) {
        int[][] dp = new int[coins.length+1][amount+1];
        for (int i=0; i<=coins.length; i++) dp[i][0] = 1;
        for (int i=1; i<=coins.length; i++){
            int coin = coins[i-1];
            for (int j=1; j<=amount; j++){
                if (j<coin) dp[i][j] = dp[i-1][j];
                else    dp[i][j] = dp[i-1][j] + dp[i][j-coin];
            }
        }
        return dp[coins.length][amount];
    }
}
