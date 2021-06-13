'''
https://leetcode.com/problems/non-overlapping-intervals/
Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
'''
'''
Time:O(nlgn)
Spcae:O(1)
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 1
        intervals.sort(key = lambda x:x[1])
        end = intervals[0][1]
        for inter in intervals[1:]:
            if inter[0]>=end:
                count += 1
                end = inter[1]
        return len(intervals)-count
