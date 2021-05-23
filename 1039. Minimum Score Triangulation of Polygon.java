/*
https://leetcode.com/problems/minimum-score-triangulation-of-polygon/
You have a convex n-sided polygon where each vertex has an integer value. 
You are given an integer array values where values[i] is the value of the ith vertex (i.e., clockwise order).

You will triangulate the polygon into n - 2 triangles. For each triangle, 
the value of that triangle is the product of the values of its vertices, 
and the total score of the triangulation is the sum of these values over all n - 2 triangles in the triangulation.
Return the smallest possible total score that you can achieve with some triangulation of the polygon.

Example 1:
Input: values = [1,2,3]
Output: 6
Explanation: The polygon is already triangulated, and the score of the only triangle is 6.
*/
/*
Time:O(n**3)
Space:O(n**2)
*/
class Solution {
    public int minScoreTriangulation(int[] v) {
        int n = v.length;
        int[][] dp = new int[n][n];
        for (int i=n-1; i>=0; i--){
            for (int j=i+2; j<n; j++){
                dp[i][j] = Integer.MAX_VALUE;
                for (int k=i+1; k<j; k++)
                    dp[i][j] = Math.min(dp[i][j], dp[i][k]+dp[k][j]+v[i]*v[j]*v[k]);
            }
        }
        return dp[0][n-1];
    }
}
