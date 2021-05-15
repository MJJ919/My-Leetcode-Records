/*
https://leetcode.com/problems/minimum-knight-moves/
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].
A knight has 8 possible moves it can make, as illustrated below. 
Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists. 

Example 1:
Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
*/
/*
*/
class Solution {
    public int minKnightMoves(int x, int y) {
        int[][] offsets = {{1, 2}, {2, 1}, {2, -1}, {1, -2},
                {-1, -2}, {-2, -1}, {-2, 1}, {-1, 2}};
        boolean[][] visited = new boolean[605][605];
        Deque<int[]> queue = new LinkedList<>();
        queue.addLast(new int[]{0, 0});
        int steps = 0;
        
        while (queue.size()>0){
            int cursize = queue.size();
            for (int i=0; i<cursize; i++){
                int[] cur = queue.removeFirst();
                if (cur[0]==x && cur[1]==y) return steps;
                
                for (int[] offset: offsets){
                    int[] next = {cur[0]+offset[0], cur[1]+offset[1]};
                    if (!visited[next[0]+302][next[1]+302]){
                        visited[next[0]+302][next[1]+302] = true;
                        queue.addLast(next);
                    }
                }
            }
            steps++;
        }
        return steps;
    }
}

/*
*/
class Solution {
    private Map<String, Integer> memo = new HashMap<>();
    
    private int dfs(int x, int y){
        String key = x+","+y;
        if (memo.containsKey(key))  return memo.get(key);
        
        if (x+y==0) return 0;
        else if (x+y==2)    return 2;
        else    {
            Integer ret = Math.min(dfs(Math.abs(x-1), Math.abs(y-2)), dfs(Math.abs(x-2), Math.abs(y-1))) + 1;
            memo.put(key, ret);
            return ret;
        }
    }
    
    public int minKnightMoves(int x, int y) {
        return dfs(Math.abs(x), Math.abs(y));
    }
}
