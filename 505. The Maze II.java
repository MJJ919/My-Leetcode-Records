/*
https://leetcode.com/problems/the-maze-ii/
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). 
The ball can go through the empty spaces by rolling up, down, left or right, 
but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the destination, 
where start = [startrow, startcol] and destination = [destinationrow, destinationcol], 
return the shortest distance for the ball to stop at the destination. If the ball cannot stop at destination, return -1.

The distance is the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included).
You may assume that the borders of the maze are all walls (see examples).

Example 1:
Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
Output: 12
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
The length of the path is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.
*/
/*
Time:O(mn lg(mn))
Space:O(mn)
*/
class Solution {
    int[][] dir = {{0,1}, {0,-1}, {1,0}, {-1, 0}};
    public int shortestDistance(int[][] maze, int[] start, int[] d) {
        int m = maze.length;
        int n = maze[0].length;
        int [][] memo = new int[m][n];
        for (int[] row: memo)   Arrays.fill(row, Integer.MAX_VALUE);
        memo[start[0]][start[1]] = 0;
        find(maze, start, memo);
        return memo[d[0]][d[1]]==Integer.MAX_VALUE? -1:memo[d[0]][d[1]];            
    }
    
    private void find(int[][] maze, int[] pos, int[][] memo){
        int m = maze.length;
        int n = maze[0].length;
        PriorityQueue<int[]> q = new PriorityQueue<>((a, b) -> (a[2]-b[2]));
        q.offer(new int[]{pos[0], pos[1], 0});
        while (!q.isEmpty()){
            int[] cur = q.poll();
            for (int[] d:dir){
                int x = cur[0], y = cur[1], count=0;
                while (x+d[0]>=0 && x+d[0]<m && y+d[1]>=0 && y+d[1]<n && maze[x+d[0]][y+d[1]]!=1){
                    x = x+d[0];
                    y = y+d[1];
                    count++;
                }
                if (memo[cur[0]][cur[1]]+count<memo[x][y]){
                    memo[x][y] = memo[cur[0]][cur[1]]+count;
                    q.offer(new int[]{x, y, memo[x][y]});
                }
            }
        }
    }
}
