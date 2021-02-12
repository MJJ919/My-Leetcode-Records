'''
https://leetcode.com/problems/course-schedule/
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
'''
class Solution:
    def canFinish(self, num: int, pre: List[List[int]]) -> bool:
        d = defaultdict(list)
        for [i,j] in pre:
            d[j].append(i)
        path = [False]*num
        checked = [False]*num
        
        def isCyclic(cur, path, checked):
            if checked[cur]:    return False
            if path[cur]:   return True
            path[cur] = True
            ret = False
            for pre in d[cur]:
                ret = isCyclic(pre, path, checked)
                if ret: break
            path[cur] = False
            checked[cur] = True
            return ret
                
        for cur in range(num):
            if isCyclic(cur, path, checked):
                return False
        return True
