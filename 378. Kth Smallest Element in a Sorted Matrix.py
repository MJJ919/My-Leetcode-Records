'''
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.
'''
'''
Time:O(1)
Space:O(1)
'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                l.append(matrix[i][j])
        l.sort()
        return l[k-1]
