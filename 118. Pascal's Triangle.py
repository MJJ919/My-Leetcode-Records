'''
https://leetcode.com/problems/pascals-triangle/
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
'''
Time:O(n**2)
Space:O(n**2)
'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]for _ in range(numRows)]
        for i in range(1,numRows):
            for j in range(1,i):
                res[i].append(res[i-1][j-1]+res[i-1][j])
            res[i].append(1)
        return res
