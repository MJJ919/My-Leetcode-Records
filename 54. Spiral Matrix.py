'''
https://leetcode.com/problems/spiral-matrix/
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
'''
Time:O(N)
Space:O(1)
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def spiral(r1, r2, c1, c2):
            for c in range(c1, c2+1):
                yield r1,c
            for r in range(r1+1, r2+1):
                yield r, c2
            if c1<c2 and r1<r2:
                for c in range(c2-1, c1,-1):
                    yield r2, c
                for r in range(r2, r1, -1):
                    yield r, c1
                
        r1, r2 = 0, len(matrix)-1
        c1, c2 = 0, len(matrix[0])-1
        res = []
        while r1<=r2 and c1<=c2:
            for r, c in spiral(r1, r2, c1, c2):
                res.append(matrix[r][c])
            r1, r2 = r1+1, r2-1
            c1, c2 = c1+1, c2-1
        return res

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix or not matrix[0]: return res
        left, right, up, down = 0, len(matrix[0])-1, 0, len(matrix)-1
        while left<right and up<down:
            for j in range(left, right):
                res.append(matrix[up][j])
            for i in range(up, down):
                res.append(matrix[i][right])
            for j in range(right, left, -1):
                res.append(matrix[down][j])
            for i in range(down, up, -1):
                res.append(matrix[i][left])
            left, right, up, down = left+1, right-1, up+1, down-1
        if left==right:
            for i in range(up, down+1):
                res.append(matrix[i][left])
        elif up==down:
            for j in range(left, right+1):
                res.append(matrix[up][j])
        return res
