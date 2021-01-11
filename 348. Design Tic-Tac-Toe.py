'''
https://leetcode.com/problems/design-tic-tac-toe/
Assume the following rules are for the tic-tac-toe game on an n x n board between two players:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves are allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.

Implement the TicTacToe class:
TicTacToe(int n) Initializes the object the size of the board n.
int move(int row, int col, int player) Indicates that player with id player plays at the cell (row, col) of the board. 
The move is guaranteed to be a valid move.
'''
'''
Time:O(1)
Space:O(n)
'''
class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.row = [0]*n
        self.col = [0]*n
        self.dig1 = self.dig2 = 0

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.col[col]+=1 if player==1 else -1
        self.row[row]+=1 if player==1 else -1
        if row+col==self.n-1:
            self.dig1+=1 if player==1 else -1
        if row==col:
            self.dig2+=1 if player==1 else -1
        if abs(self.row[row])==self.n or abs(self.col[col])==self.n or abs(self.dig1)==self.n or abs(self.dig2)==self.n:
            return 1 if player==1 else 2
        return 0
