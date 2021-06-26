'''
https://leetcode.com/problems/number-of-islands-ii/
You are given an empty 2D binary grid grid of size m x n. 
The grid represents a map where 0's represent water and 1's represent land. 
Initially, all the cells of grid are water cells (i.e., all the cells are 0's).

We may perform an add land operation which turns the water at position into a land. 
You are given an array positions where positions[i] = [ri, ci] is the position (ri, ci) at which we should operate the ith operation.

Return an array of integers answer where answer[i] is the number of islands after turning the cell (ri, ci) into a land.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
Output: [1,1,2,3]
Explanation:
Initially, the 2d grid is filled with water.
- Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land. We have 1 island.
- Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land. We still have 1 island.
- Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land. We have 2 islands.
- Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land. We have 3 islands.
'''
'''
Time:O(m*n+L)
Space:O(m*n)
'''
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        res = []
        parent = [i for i in range(m*n)]
        count = 0
        seen = [[False for _ in range(n)]for _ in range(m)]
        def find(num):
            if parent[num]!=num:
                parent[num] = find(parent[num])
            return parent[num]
        
        def union(n1, n2):
            parent[n1] = n2
            
        for p0, p1 in positions:
            if seen[p0][p1]:
                res.append(count)
                continue
            seen[p0][p1] = True
            count += 1
            for row, col in ((p0+1, p1), (p0-1, p1), (p0, p1+1), (p0, p1-1)):
                if row<0 or row==m or col<0 or col==n or not seen[row][col]:    continue
                root1 = find(row*n+col)
                root2 = find(p0*n+p1)
                if root1!=root2:
                    union(root2, root1)
                    count -= 1
            res.append(count)
        return res
        
