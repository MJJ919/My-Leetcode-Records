'''
Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below. 
More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def minimumTotal(self, t: List[List[int]]) -> int:
        if len(t)==1:
            return t[0][0]
        for i in range(1, len(t)):
            t[i][0] = t[i][0]+t[i-1][0]
            t[i][-1] = t[i][-1]+t[i-1][-1]
            for j in range(1,len(t[i])-1):
                t[i][j] = t[i][j]+min(t[i-1][j-1], t[i-1][j])
        return min(t[-1])
