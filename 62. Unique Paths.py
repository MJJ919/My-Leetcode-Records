'''
https://leetcode.com/problems/unique-paths/
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?
'''

'''
This is a math method.
Time:O(M*N)
Space:O(M*N)
'''
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        d = [[1]*n for i in range(m)] # set all the square to be 1.
        for i in range(1,m):
            for j in range(1,n):
                d[i][j] = d[i-1][j]+d[i][j-1]
        
        return d[m-1][n-1]
