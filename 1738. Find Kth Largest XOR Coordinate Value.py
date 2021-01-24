'''
https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/
You are given a 2D matrix of size m x n, consisting of non-negative integers. You are also given an integer k.
The value of coordinate (a, b) of the matrix is the XOR of all matrix[i][j] where 0 <= i <= a < m and 0 <= j <= b < n (0-indexed).
Find the kth largest value (1-indexed) of all the coordinates of matrix.

Example 1:
Input: matrix = [[5,2],[1,6]], k = 1
Output: 7
Explanation: The value of coordinate (0,1) is 5 XOR 2 = 7, which is the largest value.
'''
'''
Time:O(nlgn)
Space:O(n)
'''
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        r,c = len(matrix), len(matrix[0])
        ans = []
        for i in range(r):
            for j in range(c):
                if i:
                    matrix[i][j] ^= matrix[i-1][j]
                if j:
                    matrix[i][j] ^= matrix[i][j-1]
                if i and j:
                    matrix[i][j] ^= matrix[i-1][j-1]
                ans.append(matrix[i][j])
        return sorted(ans)[-k]
