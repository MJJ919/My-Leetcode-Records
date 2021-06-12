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
        for inter in intervals:
            if not new or inter[1]<new[0]:
                res.append(inter)
            elif inter[0]>new[1]:
                res.append(new)
                res.append(inter)
                new = None
            else:
                new[0] = min(new[0], inter[0])
                new[1] = max(new[1], inter[1])
        if new:
            res.append(new)
        return res
    
'''
Time:O(nlgn)
Space:O(n)
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        res = []
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0]>res[-1][1]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])
        return res
