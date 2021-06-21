'''
https://leetcode.com/problems/number-of-1-bits/
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
Example 1:
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
'''
'''
Time:O(1)
Space:O(1)
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            if n & 1:
                res += 1
            n = n>>1
        return res
    
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        mask = 1
        for _ in range(32):
            if n&mask:
                count += 1
            mask <<= 1
        return count
