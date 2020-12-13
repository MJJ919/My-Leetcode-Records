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
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        a = [[] for x in xrange(numRows)]
        for i in range(numRows):
            for n in range(i+1):
                if n == 0 or n == i:
                    a[i].append(1)
                else:
                    a[i].append(a[i-1][n-1]+a[i-1][n])
        return a
