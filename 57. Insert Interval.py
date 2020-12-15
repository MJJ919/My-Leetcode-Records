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

Example 3:
Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]

Example 4:
Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]

Example 5:
Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        ns, ne = newInterval
        i, n = 0, len(intervals)
        output = []
        while i<n and ns>intervals[i][0]:
            output.append(intervals[i])
            i += 1
        if not output or output[-1][1]<ns:
            output.append(newInterval)
        else:
            output[-1][1]=max(ne,output[-1][1])
            
        while i<n:
            s, e = intervals[i]
            if s>output[-1][1]:
                output.append(intervals[i])
            elif s<=output[-1][1]:
                output[-1][1] = max(e,output[-1][1])
            i += 1
        return output
