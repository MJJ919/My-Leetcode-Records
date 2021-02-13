'''
https://leetcode.com/problems/trapping-rain-water/
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n==0:    return 0
        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]
        maxleft, maxright = height[0], height[-1]
        for i in range(n):
            maxleft = max(maxleft, height[i])
            maxright = max(maxright, height[n-i-1])
            left[i], right[n-i-1] = maxleft, maxright
        res = 0
        for i in range(n):
            res += min(left[i], right[i])-height[i]
        return res
