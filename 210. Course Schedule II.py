'''
https://leetcode.com/problems/course-schedule-ii/
There are a total of n courses you have to take labelled from 0 to n - 1.
Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] this means you must take the course bi before the course ai.
Given the total number of courses numCourses and a list of the prerequisite pairs, return the ordering of courses you should take to finish all courses.
If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
'''
'''
Time:O(E+V)
Space:O(E+V)
'''
class Solution:
    def findOrder(self, num: int, pre: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        res = []
        count = 0
        q = deque()
        memo = [0 for _ in range(num)]
        for i in range(len(pre)):
            d[pre[i][1]].append(pre[i][0])
            memo[pre[i][0]] += 1
        for i in range(num):
            if memo[i] == 0:
                q.append(i)
        while q:
            cur = q.popleft()
            count += 1
            res.append(cur)
            for c in d[cur]:
                memo[c] -= 1
                if memo[c]==0:
                    q.append(c)
        return res if count==num else []
