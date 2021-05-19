/*
https://leetcode.com/problems/stone-game-ii/
Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, 
and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 
Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).
The game continues until all the stones have been taken.
Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

Example 1:
Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. 
Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. 
In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 
*/
/*
Time:O(n**2)
Space:O(n**2)
*/
class Solution {
    public int stoneGameII(int[] piles) {
        int n = piles.length;
        int[] sum = new int[n];
        for (int i=n-1; i>=0; i--){
            if (i==n-1) sum[i] = piles[i];
            else    sum[i] = sum[i+1]+piles[i];
        }
        int[][] memo = new int[n][n];
        return helper(piles, 0, 1, memo, sum);
    }
    
    public int helper(int[] p, int index, int m, int[][] memo, int[] sum){
        if (index == p.length)  return 0;
        if (p.length-index <= 2*m)  return sum[index];
        if (memo[index][m]!=0)  return memo[index][m];
        int min = Integer.MAX_VALUE;
        for (int i=1; i<=2*m; i++){
            min = Math.min(helper(p, index+i, Math.max(m, i), memo, sum), min);
        }
        return memo[index][m] = sum[index] - min;
    }
}
