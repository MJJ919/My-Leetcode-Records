'''
https://leetcode.com/problems/remove-covered-intervals/
Given a list of intervals, remove all intervals that are covered by another interval in the list.
Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.
After doing so, return the number of remaining intervals.

Example 1:
Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
'''
'''
Time:O(nlgn)
Space:O(1)
'''
class Solution:
    def removeCoveredIntervals(self, inter: List[List[int]]) -> int:
        inter = sorted(inter, key = lambda x:(x[0], -x[1]))
        end = 0
        count = 0
        for i in range(len(inter)):
            if inter[i][1]>end:
                count += 1
                end = inter[i][1]
        return count
