'''
https://leetcode.com/problems/spiral-matrix-ii/
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
'''
'''
Time:O(n^2)
Space:O(1)
'''
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = [[0 for _ in range(n)] for _ in range(n)]
        left, right, up, down = 0, n - 1, 0, n - 1
        count = 1
        while left <= right and up <= down:
            for j in range(left, right):
                m[up][j] = count
                count += 1
            for i in range(up, down):
                m[i][right] = count
                count += 1
            for j in range(right, left, -1):
                m[down][j] = count
                count += 1
            for i in range(down, up, -1):
                m[i][left] = count
                count += 1
            left, right, up, down = left + 1, right - 1, up + 1, down - 1
        if n%2==1:
            mid = n//2
            m[mid][mid]=count
        return m
