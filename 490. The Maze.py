'''
https://leetcode.com/problems/the-maze/
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). 
The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. 
When the ball stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the destination, 
where start = [startrow, startcol] and destination = [destinationrow, destinationcol], 
return true if the ball can stop at the destination, otherwise return false.

You may assume that the borders of the maze are all walls (see examples).

Example 1:
Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
Output: true
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
'''
'''
BFS
Time:O(mn)
Space:O(mn)
'''
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        s = deque()
        s.append(start)
        seen = set()
        seen.add((start[0], start[1]))
        move = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while s:
            for _ in range(len(s)):
                node = s.popleft()
                row, col = node[0], node[1]
                if node == destination:
                    return True
                for i, j in move:
                    r, c = row, col
                    while r+i>=0 and r+i<len(maze) and c+j>=0 and c+j<len(maze[0]) and maze[r+i][c+j]!=1:
                        r, c = r+i, c+j
                    if (r, c) not in seen:
                        s.append([r, c])
                        seen.add((r, c))
        return False
                    
'''
DFS
Time:O(mn)
Space:O(mn)
'''
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = set()
        d = ((1,0), (-1,0), (0,1), (0,-1))
        m = len(maze)
        n = len(maze[0])
        def search(i, j):
            if (i, j) in visited:   return False
            if [i, j]==destination: return True
            visited.add((i, j))
            for (a,b) in d:
                newx = i; newy = j
                while 0<=newx+a<m and 0<=newy+b<n and maze[newx+a][newy+b]==0:
                    newx += a
                    newy += b
                if search(newx, newy):  return True
            return False
        return search(start[0], start[1])
