'''
https://leetcode.com/problems/word-search/
The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
'''
'''
Time:O(N⋅3^L)
Space:O(L)
'''
#BACKTRACKING
ss Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.row, self.col = len(board), len(board[0])
        self.board = board
        for row in range(self.row):
            for col in range(self.col):
                if self.bt(row,col,word):
                    return True
        
    def bt(self, r, c, word):
        if not word:    return True
        elif r<0 or r==self.row or c<0 or c==self.col or self.board[r][c]!=word[0]:    return False
            
        res = False
        self.board[r][c]='#'
        for i, j in [(0,1), (1,0), (-1,0), (0,-1)]:
            res = self.bt(r+i, c+j, word[1:])
            if res: break
        self.board[r][c]=word[0]
        return res
