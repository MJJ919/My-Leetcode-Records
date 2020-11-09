'''

Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

xample 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''

'''
Time:O(NlogN)
Space:O(n)
'''
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda x:x[0])
        merge=[]
        for i in intervals:
            if not merge or merge[-1][1]<i[0]:
                merge.append(i)
            else:
                merge[-1][1] = max(merge[-1][1],i[1])
        return merge
