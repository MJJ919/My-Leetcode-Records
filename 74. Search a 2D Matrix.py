'''
https://leetcode.com/problems/search-a-2d-matrix/
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 
Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
Output: false
'''
'''
Method below first find the row target might in. Then 2 pointers are used to target whether this target in the certain row.
Time:O(m+logn)
Space:O(1)
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix[-1][-1]<target:
            return False
        a = 0
        while a<len(matrix):
            if matrix[a][-1]>=target:
                break
            else:
                a += 1
        m, n = 0, len(matrix[a])
        while m<=n:
            mid = (m+n)//2
            if matrix[a][mid] == target:
                return True
            elif matrix[a][mid] > target:
                n = mid-1
            else:
                m = mid+1
        return False

'''
Time:O(lg(mn))
Space:O(1)
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix[-1][-1]<target:   return False
        m, n = len(matrix), len(matrix[0])
        
        left, right = 0, m*n-1
        while left<=right:
            mid = (left+right)//2
            col, row = mid//n, mid%n
            if matrix[col][row]==target:
                return True
            elif matrix[col][row]>target:
                right = mid-1
            else:
                left = mid+1
        return False
