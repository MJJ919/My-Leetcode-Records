'''
https://leetcode.com/problems/single-threaded-cpu/
'''
'''
Time:O(nlgn)
Space:O(n)
'''
class Solution:
    def getOrder(self, tasks):
        t = []
        res = []
        for idx, task in enumerate(tasks):
            t.append([task[0], task[1], idx])
        t = sorted(t)
        start = t[0][0]
        heap = []
        i = 0
        while len(res) < len(t):
            while i < len(t) and t[i][0] <= start:
                heapq.heappush(heap, [t[i][1], t[i][2]])
                i += 1
            if heap:
                task = heapq.heappop(heap)
                res.append(task[1])
                start += task[0]
            elif i < len(t):
                start = t[i][0]
        return res
