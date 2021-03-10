'''
https://leetcode.com/problems/insert-interval/
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def insert(self, intervals: List[List[int]], new: List[int]) -> List[List[int]]:
        res = []
        start, end = new[0], new[1]
        i = 0
        while i<len(intervals) and intervals[i][0]<start:
                res.append(intervals[i])
                i += 1
        if not res or res[-1][1]<start:
            res.append(new)
        else:
            res[-1][1] = max(res[-1][1], end)
            
        while i<len(intervals):
            if res[-1][1]<intervals[i][0]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            i += 1
        return res
