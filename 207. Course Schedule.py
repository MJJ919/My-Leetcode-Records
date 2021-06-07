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
        memo = [0 for _ in range(num)]
        q = deque()
        count = 0
        for i in range(len(pre)):
            d[pre[i][1]].append(pre[i][0])
            memo[pre[i][0]] += 1
        for i in range(num):
            if memo[i]==0:
                q.append(i)
        while q:
            cur = q.popleft()
            count += 1
            for c in d[cur]:
                memo[c] -= 1
                if memo[c]==0:
                    q.append(c)
        return count==num
