'''
https://leetcode.com/problems/bitwise-and-of-numbers-range/
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:
Input: [5,7]
Output: 4
'''
'''
Time:O(1)
Space:O(1)
'''
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0
        while m<n:
            m = m>>1
            n = n>>1
            shift += 1
        return m<<shift
