'''
https://leetcode.com/problems/surrounded-regions/
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:   return
        m, n = len(board), len(board[0])
        def find(row, col):
            if 0<=row<m and 0<=col<n and board[row][col]=='O':
                board[row][col]='A'
                for (p, q) in ((1,0), (-1,0), (0,1), (0,-1)):
                    find(row+p, col+q)
            
        for i in range(m):
            for j in [0, n-1]:
                if board[i][j]=='O':
                    find(i, j)
        for i in [0, m-1]:
            for j in range(n):
                if board[i][j]=='O':
                    find(i, j)
        for i in range(m):
            for j in range(n):
                if board[i][j]=='A':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'
