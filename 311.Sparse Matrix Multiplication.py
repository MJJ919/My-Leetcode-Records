'''
https://leetcode.com/problems/sparse-matrix-multiplication/
Given two sparse matrices A and B, return the result of AB.
You may assume that A's column number is equal to B's row number.
'''
'''
Time:O(n**2)
Space:O(n**2)
'''
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        l = [[0 for _ in range(len(B[0]))]for _ in range(len(A))]
        for i,row in enumerate(A):
            for k, eleA in enumerate(row):
                if eleA:
                    for j, eleB in enumerate(B[k]):
                        l[i][j] += eleA*eleB
        return l
