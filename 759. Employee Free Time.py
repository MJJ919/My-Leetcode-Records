'''
https://leetcode.com/problems/employee-free-time/
We are given a list schedule of employees, which represents the working time for each employee.
Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.
(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. 
For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  
Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

Example 1:
Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.
'''
'''
Time:O(nlgn)
Space:O(n)
'''

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        inter = sorted([i for s in schedule for i in s], key = lambda x:x.start)
        res = []
        pre = inter[0]
        for i in inter[1:]:
            if pre.end<i.start:
                res.append(Interval(pre.end, i.start))
                pre = i
            elif i.end>pre.end:
                pre.end = i.end
        return res
