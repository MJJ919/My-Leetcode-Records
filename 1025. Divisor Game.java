/*
https://leetcode.com/problems/divisor-game/
Alice and Bob take turns playing a game, with Alice starting first.
Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < n and n % x == 0.
Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.

Return true if and only if Alice wins the game, assuming both players play optimally.

Example 1:
Input: n = 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.
*/
/*
Time:O(n**2)
Space:O(n)
*/
class Solution {
    public boolean divisorGame(int n) {
        Boolean[] memo = new Boolean[n+1];
        return helper(n, memo);
    }
    
    public boolean helper(int n, Boolean[] memo){
        if (n==1)    return false;
        if (memo[n] != null)  return memo[n];
        boolean canwin = false;
        for (int i=1; i<=n/2; i++){
            if (n%i==0 && !helper(n-i, memo)){
                canwin = true;
                break;
            }
        }
        memo[n] = canwin;
        return memo[n];
    }
}
