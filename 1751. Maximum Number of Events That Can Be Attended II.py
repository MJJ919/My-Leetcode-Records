'''
https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/
'''
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key = lambda x:x[1])
        dp1, dp2 = [[0,0]], [[0,0]]
        for _ in range(k):
            for start, end, value in events:
                idx = bisect.bisect(dp1, [start])-1
                if dp1[idx][1]+value > dp2[-1][1]:
                    dp2.append([end, dp1[idx][1]+value])
            dp1, dp2 = dp2, [[0,0]]
        return dp1[-1][-1]
