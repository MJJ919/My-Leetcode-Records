'''
https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/
You are given an undirected graph. You are given an integer n which is the number of nodes in the graph and an array edges, 
where each edges[i] = [ui, vi] indicates that there is an undirected edge between ui and vi.
A connected trio is a set of three nodes where there is an edge between every pair of them.
The degree of a connected trio is the number of edges where one endpoint is in the trio, and the other is not.
Return the minimum degree of a connected trio in the graph, or -1 if the graph has no connected trios.
'''
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        d = defaultdict(lambda: set())
        for u,v in edges:
            d[u].add(v)
            d[v].add(u)
        res = float('inf')
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                for k in range(j+1, n+1):
                    if i in d[j] and j in d[k] and k in d[i]:
                        s = len(d[i])+len(d[j])+len(d[k])-6
                        res = min(s, res)
        return res if res!=float('inf') else -1
