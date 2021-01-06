'''
https://leetcode.com/problems/perfect-squares/
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''
'''
Time:O(n**(3/2))
Space:O(n)
'''
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = [i**2 for i in range(0, int(n**0.5)+1)]
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        for i in range(1,n+1):
            for s in squares:
                if i<s:
                    break
                dp[i] = min(dp[i], dp[i-s]+1)
        return dp[-1]
