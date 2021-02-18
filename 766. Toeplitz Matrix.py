'''
https://leetcode.com/problems/toeplitz-matrix/
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

Example 1:
Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
'''
'''
Time:O(m*n)
Space:O(1)
'''
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(r==0 or c==0 or matrix[r-1][c-1]==matrix[r][c] for r, row in enumerate(matrix) for c, col in enumerate(row))
 
'''
Time:O(m*n)
Space:O(1)
'''
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for loop in range(n-1):
            temp = matrix[0][loop]
            i = 1
            while i<m and i+loop<n:
                if matrix[i][i+loop]!=temp:
                    return False
                i += 1
        for loop in range(m-1):
            temp = matrix[loop][0]
            j = 1
            while j<n and j+loop<m:
                if matrix[j+loop][j]!=temp:
                    return False
                j += 1
        return True
