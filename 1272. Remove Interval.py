'''
https://leetcode.com/problems/remove-interval/
A set of real numbers can be represented as the union of several disjoint intervals, where each interval is in the form [a, b). 
A real number x is in the set if one of its intervals [a, b) contains x (i.e. a <= x < b).

You are given a sorted list of disjoint intervals intervals representing a set of real numbers as described above, 
where intervals[i] = [ai, bi] represents the interval [ai, bi). You are also given another interval toBeRemoved.

Return the set of real numbers with the interval toBeRemoved removed from intervals. 
In other words, return the set of real numbers such that every x in the set is in intervals but not in toBeRemoved. 
Your answer should be a sorted list of disjoint intervals as described above.

Example 1:
Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
Output: [[0,1],[6,7]]
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def removeInterval(self, intervals: List[List[int]], re: List[int]) -> List[List[int]]:
        res = []
        for inter in intervals:
            if inter[0] >= re[1] or inter[1] <= re[0]:
                res.append(inter)
            else:
                if inter[0]<re[0]:
                    res.append([inter[0], re[0]])
                if inter[1]>re[1]:
                    res.append([re[1],inter[1]])
        return res
