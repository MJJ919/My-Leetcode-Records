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
        if not height:
            return 0
        n = len(height)
        left = [0]*n
        right = [0]*n
        l,r = height[0], height[n-1]
        for i in range(n):
            l = max(l,height[i])
            left[i] = l
            r = max(r, height[n-1-i])
            right[n-i-1] = r
        res = 0
        for j in range(n):
            res += min(left[j], right[j])-height[j]
        return res
