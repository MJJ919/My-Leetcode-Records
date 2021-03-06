'''
https://leetcode.com/problems/climbing-stairs/
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b = 1
        for i in range(n-1):
            c = a+b
            a = b
            b = c
        return b

'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:  return 1
        res = [0]
        res.append(1)
        res.append(2)
        for i in range(3, n+1):
            res.append(res[i-1]+res[i-2])
        return res[n]
