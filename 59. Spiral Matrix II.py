'''
https://leetcode.com/problems/spiral-matrix-ii/
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
'''
'''
Time:O(n^2)
Space:O(1)
'''
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def spiral(r1,r2,c1,c2):
            for c in range(c1, c2+1):
                yield r1, c
            for r in range(r1+1, r2+1):
                yield r, c2
            if r1<r2 and c1<c2:
                for c in range(c2-1, c1-1,-1):
                    yield r2, c
                for r in range(r2-1,r1, -1):
                    yield r, c1
            
        res = [[0for _ in range(n)]for _ in range(n)]
        num = 1
        r1, r2, c1, c2 = 0, n-1, 0, n-1
        while r1<=r2 and c1<=c2:
            for r, c in spiral(r1, r2, c1, c2):
                res[r][c] = num
                num += 1
            r1+=1; r2-=1;
            c1+=1; c2-=1;
        return res
