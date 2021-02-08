'''
https://leetcode.com/problems/paint-house-ii/
There are a row of n houses, each house can be painted with one of the k colors. 
The cost of painting each house with a certain color is different. 
You have to paint all the houses such that no two adjacent houses have the same color.
The cost of painting each house with a certain color is represented by a n x k cost matrix. 
For example, costs[0][0] is the cost of painting house 0 with color 0; 
costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Example:
Input: [[1,5,3],[2,9,4]]
Output: 5
Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5; 
             Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5. 
'''
'''
Time:O(n*k^2)
Space:O(1)
'''
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        if n==0:    return 0
        k = len(costs[0])
        for i in range(1, n):
            for j in range(k):
                best = float('inf')
                for idx in range(k):
                    if idx==j:
                        continue
                    best = min(best, costs[i-1][idx])
                costs[i][j] += best
        return min(costs[-1])

'''
Time:O(n*k)
Space:O(1)
'''
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        if n==0:    return 0
        k = len(costs[0])
        for i in range(1, n):
            fir_min = sec_min = None
            for j in range(k):
                cost = costs[i-1][j]
                if fir_min==None or cost<costs[i-1][fir_min]:
                    sec_min, fir_min = fir_min, j
                elif sec_min==None or cost<costs[i-1][sec_min]:
                    sec_min = j
            for j in range(k):
                if j==fir_min:
                    costs[i][j] += costs[i-1][sec_min]
                else:
                    costs[i][j] += costs[i-1][fir_min]
        return min(costs[-1])
