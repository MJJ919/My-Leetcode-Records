'''
https://leetcode.com/problems/connecting-cities-with-minimum-cost/
There are n cities numbered from 1 to n.
You are given connections, where each connections[i] = [city1, city2, cost] 
represents the cost to connect city1 and city2 together.  
(A connection is bidirectional: connecting city1 and city2 is the same as connecting city2 and city1.)

Return the minimum cost so that for every pair of cities, there exists a path of connections 
(possibly of length 1) that connects those two cities together.  
The cost is the sum of the connection costs used. If the task is impossible, return -1.

Example 1:
Input: n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6
Explanation: 
Choosing any 2 edges will connect all cities so we choose the minimum 2.
'''
'''
'''
class Solution:
    def minimumCost(self, n: int, c: List[List[int]]) -> int:
        visited = set()
        graph = defaultdict(list)
        edge = []
        for connection in c:
            n1 = connection[0]
            n2 = connection[1]
            dis = connection[2]
            graph[n1].append([n2, dis])
            graph[n2].append([n1, dis])
        cost = 0
        heapq.heappush(edge, [0, 1, 1])
        while edge:
            cur = heapq.heappop(edge)
            n1, n2, dis = cur[1], cur[2], cur[0]
            if n2 not in visited:
                cost += dis
                visited.add(n2)
                for e in graph[n2]:
                    heapq.heappush(edge, [e[1], n2, e[0]])
        if len(visited)==n:
            return cost
        else:
            return -1
