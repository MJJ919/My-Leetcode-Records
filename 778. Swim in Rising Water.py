'''
https://leetcode.com/problems/swim-in-rising-water/
On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).

Now rain starts to fall. At time t, the depth of the water everywhere is t. 
You can swim from a square to another 4-directionally adjacent square if and only if the elevation of 
both squares individually are at most t. You can swim infinite distance in zero time. 
Of course, you must stay within the boundaries of the grid during your swim.

You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?
Example 1:
Input: [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.

You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
'''
'''
Time:O(n*n*lgn)
Space:O(n*n)
'''
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def swim(num):
            s = [(0, 0)]
            seen = {(0, 0)}
            while s:
                r, c = s.pop()
                if r==c==n-1:
                    return True
                for row, col in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if row<n and row>=0 and col<n and col>=0 and (row,col) not in seen and grid[row][col]<=num:
                        s.append([row, col])
                        seen.add((row, col))
            return False
        
        n = len(grid)
        left, right = grid[0][0], n*n
        while left<right:
            mid = (left+right)//2
            if not swim(mid):
                left = mid+1
            else:
                right = mid
        return left

'''
Time:O(n*n*lgn)
Space:O(n*n)
'''
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        seen = {(0, 0)}
        heap = [(grid[0][0], 0, 0)]
        res = 0
        n = len(grid)
        while heap:
            time, r, c = heapq.heappop(heap)
            res = max(time, res)
            if r==c==n-1:
                return res
            for row, col in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if n>row>=0 and n>col>=0 and (row, col) not in seen:
                    seen.add((row, col))
                    heapq.heappush(heap, (grid[row][col], row, col))
