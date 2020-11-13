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
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0] or target>matrix[-1][-1]:
            return False
        if target>matrix[-1][-1]:
            return False
        for i in matrix:
            if target<i[-1]:
                a = i
                break
            elif target == i[-1]:
                return True
        i,j=0,len(a)-1
        while i<=j:
            mid=(i+j)//2
            if a[mid]<target:
                i = mid+1
            elif a[mid]>target:
                j = mid-1
            else:
                return True
        return False
