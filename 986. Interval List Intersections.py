'''
https://leetcode.com/problems/interval-list-intersections/
You are given two lists of closed intervals, firstList and secondList, 
where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. 
Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.
A closed interval [a, b] (with a < b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. 
For example, the intersection of [1, 3] and [2, 4] is [2, 3].

Example 1:
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def intervalIntersection(self, f: List[List[int]], s: List[List[int]]) -> List[List[int]]:
        res = []
        i, j = 0, 0
        while i<len(f) and j<len(s):
            start = max(f[i][0], s[j][0])
            end = min(f[i][1], s[j][1])
            if end-start>=0:
                res.append([start, end])
            if f[i][1]>s[j][1]:
                j += 1
            else:
                i += 1
        return res
