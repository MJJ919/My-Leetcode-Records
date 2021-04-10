'''
https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/
You are given an integer array coins of length n which represents the n coins that you own. The value of the ith coin is coins[i]. 
You can make some value x if you can choose some of your n coins such that their values sum up to x.
Return the maximum number of consecutive integer values that you can make with your coins starting from and including 0.

Note that you may have multiple coins of the same value.

Example 1:
Input: coins = [1,3]
Output: 2
Explanation: You can make the following values:
- 0: take []
- 1: take [1]
You can make 2 consecutive integer values starting from 0.
'''
'''
Time:O(nlgn)
Space:O(1)
'''
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        res = 1
        for coin in sorted(coins):
            if coin > res:  break
            res += coin
        return res
