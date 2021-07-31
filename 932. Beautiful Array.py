'''
https://leetcode.com/problems/beautiful-array/
An array nums of length n is beautiful if:
nums is a permutation of the integers in the range [1, n].
For every 0 <= i < j < n, there is no index k with i < k < j where 2 * nums[k] == nums[i] + nums[j].
Given the integer n, return any beautiful array nums of length n. There will be at least one valid answer for the given n.


Example 1:
Input: n = 4
Output: [2,1,4,3]
'''
'''
Time:O(n)
Space:O(nlgn)
'''
class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        memo = {1:[1]}
        def construct(n):
            if n not in memo:
                odd = [2*i-1 for i in construct((n+1)//2)]
                even = [2*i for i in construct(n//2)]
                memo[n] = odd+even
            return memo[n]
        return construct(N)
