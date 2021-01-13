'''
https://leetcode.com/problems/search-a-2d-matrix-ii/
Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example 1:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
'''
'''
Search Space Reduction.
Time:O(n+m)
Space:O(1)
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix)-1, 0
        while m>=0 and n<=len(matrix[0])-1:
            if matrix[m][n]>target:
                m -= 1
            elif matrix[m][n]<target:
                n += 1
            else:
                return True
        return False

'''
Brute Force.
Time:O(mn)
Space:O(1)
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            for j in i:
                if j > target:
                    break
                elif j == target:
                    return True
        return False
  
'''
Binary Search.
Time:O(nlgn)
Space:O(1)
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        length = len(matrix[0])
        for i in matrix:
            m, n = 0, length-1
            while m<=n:
                mid = (m+n)//2
                if i[mid]==target:
                    return True
                elif i[mid]<target:
                    m = mid+1
                else:   
                    n = mid-1
        return False
