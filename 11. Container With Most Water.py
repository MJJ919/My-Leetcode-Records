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
        a, b = 0, len(height)-1
        area = 0
        while a<b:
            area = max(area, min(height[a], height[b])*(b-a))
            if height[a] < height[b]:
                a += 1
            else:
                b -= 1
        return area
