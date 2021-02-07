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
class Solution:
    def numSquares(self, n: int) -> int:
        sqr_num = [i*i for i in range(floor(sqrt(n))+1)]
        dp = [float('inf') for _ in range(n+1)]
        dp[0] = 0
        for i in range(1, n+1):
            for num in sqr_num:
                if i<num:   break
                dp[i] = min(dp[i], dp[i-num]+1)
        return dp[-1]
    
'''
'''
class Solution:
    def numSquares(self, n: int) -> int:
        sqr_num = [i*i for i in range(1, int(sqrt(n))+1)]
        
        def divide(count, n):
            if count==1:
                return n in sqr_num
            for num in sqr_num:
                if divide(count-1, n-num):
                    return True
            return False
            
        for count in range(1, n+1):
            if divide(count, n):
                return count
