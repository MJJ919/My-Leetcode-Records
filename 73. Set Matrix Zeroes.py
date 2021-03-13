'''
https://leetcode.com/problems/set-matrix-zeroes/
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.
'''
'''
Time:O(m*n)
Space:O(m+n)
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r, c = len(matrix), len(matrix[0])
        row, col = set(), set()
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        for i in range(r):
            for j in range(c):
                if i in row or j in col:
                    matrix[i][j] = 0
'''
Time:O(m*n)
Space:O(1)
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        iscol = False
        for i in range(m):
            if matrix[i][0]==0:
                iscol = True
            for j in range(1, n):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if matrix[0][0]==0:
            for j in range(n):
                matrix[0][j]=0 
        if iscol:
            for i in range(m):
                matrix[i][0]=0
