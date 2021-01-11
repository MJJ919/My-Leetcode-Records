'''
https://leetcode.com/problems/range-sum-query-2d-immutable/
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
'''
'''
Time:O(mn)
Space:O(mn)
'''
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return
        self.m = [[0 for _ in range(len(matrix[0])+1)]for _ in range(len(matrix)+1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.m[i+1][j+1] = self.m[i+1][j]+self.m[i][j+1]+matrix[i][j]-self.m[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.m[row2+1][col2+1]-self.m[row1][col2+1]-self.m[row2+1][col1]+self.m[row1][col1]
