'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.
'''

'''
Method below uses 2 pointers.
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        mx, i,j = 0, 0, len(height)-1
        while i<j:
            a = min(height[i],height[j])
            mx = max(mx, (j-i)*a)
            if a==height[i]:
                i = i+1
            else:
                j = j-1
        return mx
