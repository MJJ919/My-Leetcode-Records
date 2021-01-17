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
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pre = [1]
        cur = []
        for i in range(1,rowIndex+1):
            cur = [1 for _ in range(i+1)]
            for j in range(1,i):
                cur[j] = pre[j-1]+pre[j]
            pre = cur
        return pre
