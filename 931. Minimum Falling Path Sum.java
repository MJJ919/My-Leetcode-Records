/*
https://leetcode.com/problems/minimum-falling-path-sum/
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
A falling path starts at any element in the first row and chooses the element 
in the next row that is either directly below or diagonally left/right. 
Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

Example 1:
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum underlined below:
[[2,1,3],      [[2,1,3],
 [6,5,4],       [6,5,4],
 [7,8,9]]       [7,8,9]]
*/
/*
Time:O(mn)
Space:O(1)
*/
class Solution {
    public int minFallingPathSum(int[][] matrix) {
        int row = matrix.length;
        int col = row>0? matrix[0].length:0;
        for (int i=1; i<row; i++){
            for (int j=0; j<col; j++){
                matrix[i][j] += Math.min(matrix[i-1][Math.max(0, j-1)], Math.min(matrix[i-1][j], matrix[i-1][Math.min(j+1, col-1)]));
            }
        }
        int res = Integer.MAX_VALUE;
        for (int i=0; i<col; i++)
            res = Math.min(matrix[row-1][i], res);
        return res;
    }
}
