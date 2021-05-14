/*
https://leetcode.com/problems/nim-game/
You are playing the following Nim Game with your friend:
Initially, there is a heap of stones on the table.
You and your friend will alternate taking turns, and you go first.
On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
The one who removes the last stone is the winner.
Given n, the number of stones in the heap, return true if you can win the game assuming both you and your friend play optimally, otherwise return false.
*/
/*
Time: O(1)
Space: O(1)
*/
class Solution {
    public boolean canWinNim(int n) {
        return n%4==0? false:true;
    }
}

/*
Time: O(n)
Space: O(n)
*/
class Solution {
    public boolean canWinNim(int n) {
        if (n==1 || n==2 || n==3)   return true;
        boolean[] dp = new boolean[n];
        dp[0] = dp[1] = dp[2] = true;
        for (int i=3; i<n; i++)
            dp[i] = !(dp[i-3] && dp[i-2] && dp[i-1]);
        return dp[n-1];
    }
}
