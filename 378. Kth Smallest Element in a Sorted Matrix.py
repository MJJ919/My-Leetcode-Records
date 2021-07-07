'''
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.
'''
'''
Time:X+Klog(X).  X=min(K,N);
Space:O(X)
'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        l = []
        for i in range(min(n, k)):
            heapq.heappush(l, (matrix[i][0], i, 0))
        while k:
            num, r, c = heapq.heappop(l)
            if c<n-1:
                heapq.heappush(l, (matrix[r][c+1], r, c+1))
            k -= 1
        return num
