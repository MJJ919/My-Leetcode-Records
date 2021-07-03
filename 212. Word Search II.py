'''
https://leetcode.com/problems/word-search-ii/
Given an m x n board of characters and a list of strings words, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, 
where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
'''
'''
Time:
Space:O(n)
'''
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = {}
        def add(word, node):
            for w in word:
                if w not in node:
                    node[w] = {}
                node = node[w]
            node['$'] = True
        
        def search(s, i, j, node):
            letter = board[i][j]
            s += letter
            board[i][j] = '#'
            if '$' in node[letter] and s not in res:
                res.add(s)
            for r, c in ((i+1, j), (i, j+1), (i-1, j), (i, j-1)):
                if r>=0 and r<len(board) and c>=0 and c<len(board[0]) and board[r][c] in node[letter]:
                    search(s, r, c, node[letter])
            board[i][j] = letter
        
        for word in words:
            add(word, root)
            
        res = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root:
                    search('', i, j, root)
        return list(res)
