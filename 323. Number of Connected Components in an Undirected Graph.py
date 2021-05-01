'''
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] 
indicates that there is an edge between ai and bi in the graph.
Return the number of connected components in the graph.

Example 1:
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
'''
'''
Time:O(E+V)
Space:O(E+V)
'''
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        graph = [[]for _ in range(n)]
        seen = [False for _ in range(n)]
        for [a, b] in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node):
            for i in graph[node]:
                if not seen[i]:
                    seen[i] = True
                    dfs(i)
            
        for i in range(n):
            if not seen[i]:
                res += 1
                seen[i] = True
                dfs(i)
        return res
