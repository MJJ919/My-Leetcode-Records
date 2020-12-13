'''
https://leetcode.com/problems/pascals-triangle-ii/
Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.
Notice that the row index starts from 0.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]
'''
'''
Time:O(n**2)
Space:O(n)
'''
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for i in range(rowIndex):
            for j in range(i,0,-1):
                row[j]=row[j]+row[j-1]
            row.append(1)
        return row
