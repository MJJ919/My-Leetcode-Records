'''
There is a fence with n posts, each post can be painted with one of the k colors.
You have to paint all the posts such that no more than two adjacent fence posts have the same color.
Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.

Example:
Input: n = 3, k = 2
Output: 6
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n==0:
            return 0
        if n==1:
            return k
        pre, cur = k, k*k
        for i in range(n-2):
            pre, cur = cur, (cur+pre)*(k-1)
        return cur
