'''
https://leetcode.com/problems/paint-house/
There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. 
The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. 
For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Example 1:
Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
Minimum cost: 2 + 5 + 3 = 10.
'''
'''
Dynamic Programming.
Time:O(n)
Space:O(1)
'''
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:    return 0
        dp = [[0 for _ in range(3)]for _ in range(len(costs))]
        dp[0] = costs[0]
        for i in range(1, len(costs)):
            dp[i][0] = costs[i][0]+min(dp[i-1][1], dp[i-1][2])
            dp[i][1] = costs[i][1]+min(dp[i-1][0], dp[i-1][2])
            dp[i][2] = costs[i][2]+min(dp[i-1][1], dp[i-1][0])
        return min(dp[-1])

'''
Memoization.
Time:O(n)
Space:O(n)
'''
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        def paint(n, color):
            if (n, color) in self.memo:
                return self.memo[(n, color)]
            money = costs[n][color]
            if n==len(costs)-1:
                pass
            elif color==0:
                money += min(paint(n+1, 1), paint(n+1, 2))
            elif color==1:
                money += min(paint(n+1, 0), paint(n+1, 2))
            elif color==2:
                money += min(paint(n+1, 1), paint(n+1, 0))
            self.memo[(n,color)] = money
            return money
        
        if costs == []:   return 0
        self.memo = {}
        return min(paint(0,0), paint(0,1), paint(0,2))
