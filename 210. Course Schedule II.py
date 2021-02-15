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
    white = 1
    gray = 2
    black = 3
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for cur, pre in prerequisites:
            adj[pre].append(cur)
        order = []
        self.ispossible = True
        color = {k:Solution.white for k in range(numCourses)}
        
        def dfs(node):
            if not self.ispossible:
                return
            color[node] = Solution.gray
            if node in adj:
                for neighbor in adj[node]:
                    if color[neighbor]==Solution.white:
                        dfs(neighbor)
                    elif color[neighbor]==Solution.gray:
                        self.ispossible = False
            color[node] = Solution.black
            order.append(node)
            
        for node in range(numCourses):
            if color[node] == Solution.white:
                dfs(node)
        return order[::-1] if self.ispossible else []
