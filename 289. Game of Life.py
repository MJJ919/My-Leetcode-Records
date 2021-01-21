'''
https://leetcode.com/problems/game-of-life/
'''
'''
Time:O(m*n)
Space:O(m*n)
'''
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        row = len(board)
        col = len(board[0])
        copyboard = copy.deepcopy(board)
        for i in range(row):
            for j in range(col):
                liven = 0
                for neighbor in neighbors:
                    r = i + neighbor[0]
                    c = j + neighbor[1]
                    if (r>=0 and r<row) and (c>=0 and c<col) and (copyboard[r][c] == 1):
                        liven += 1
                if copyboard[i][j]==1 and (liven<2 or liven>3):
                    board[i][j] = 0
                if copyboard[i][j]==0 and liven == 3:
                    board[i][j] =1
