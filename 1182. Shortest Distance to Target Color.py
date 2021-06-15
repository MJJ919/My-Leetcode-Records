'''
https://leetcode.com/problems/shortest-distance-to-target-color/
You are given an array colors, in which there are three colors: 1, 2 and 3.
You are also given some queries. Each query consists of two integers i and c, 
return the shortest distance between the given index i and the target color c. If there is no solution return -1.

Example 1:
Input: colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
Output: [3,0,3]
Explanation: 
The nearest 3 from index 1 is at index 4 (3 steps away).
The nearest 2 from index 2 is at index 2 itself (0 steps away).
The nearest 1 from index 6 is at index 3 (3 steps away).
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        n = len(colors)
        left = [0, 0, 0]
        right = [n-1, n-1, n-1]
        dis = [[-1 for _ in range(n)]for _ in range(3)]
        for i in range(n):
            c = colors[i]-1
            for l in range(left[c], i+1):
                dis[c][l] = i-l
            left[c] = i+1
        for j in range(n-1, -1, -1):
            c = colors[j]-1
            for r in range(right[c], j-1, -1):
                if dis[c][r] == -1 or dis[c][r]>r-j:
                    dis[c][r] = r-j
            right[c] = j-1
        return [dis[color-1][pos] for [pos, color] in queries]
      
'''
Time:O(Qlgn + n)
Space:O(n)
'''
class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for idx, color in enumerate(colors):
            d[color].append(idx)
            
        def search(q):
            pos = bisect.bisect_left(d[q[1]], q[0])
            if pos==len(d[q[1]]):
                return q[0] - d[q[1]][-1]
            elif d[q[1]][pos]==q[0]:
                return 0
            else:
                return min(abs(d[q[1]][pos-1]-q[0]), abs(d[q[1]][pos]-q[0]))
            
        
        res = []
        for query in queries:
            if query[1] not in d:
                res.append(-1)
            else:
                res.append(search(query))
        return res
