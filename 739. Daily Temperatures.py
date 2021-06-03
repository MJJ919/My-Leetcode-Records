'''
https://leetcode.com/problems/daily-temperatures/
Given an array of integers temperatures represents the daily temperatures, return an array answer 
such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        s = deque()
        res = [0 for _ in range(len(t))]
        for i in range(len(t)-1, -1, -1):
            temp = t[i]
            while s and t[s[-1]]<=temp:
                s.pop()
            if s:
                res[i] = s[-1]-i
            s.append(i)
        return res
