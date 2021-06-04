'''
https://leetcode.com/problems/largest-rectangle-in-histogram/
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
return the area of the largest rectangle in the histogram. 

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        s = deque()
        res = 0
        for i in range(len(h)):
            while s and h[s[-1]]>=h[i]:
                idx = s.pop()
                if s:
                    length = i - s[-1] - 1
                else:
                    length = i
                res = max(res, length*h[idx])
            s.append(i)
            
        while s:
            idx = s.pop()
            if s:
                length = len(h) - s[-1] - 1
            else:
                length = len(h)
            res = max(res, length*h[idx])
        return res
