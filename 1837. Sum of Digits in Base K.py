'''
https://leetcode.com/problems/sum-of-digits-in-base-k/
Given an integer n (in base 10) and a base k, return the sum of the digits of n after converting n from base 10 to base k.
After converting, each digit should be interpreted as a base 10 number, and the sum should be returned in base 10.

Example 1:
Input: n = 34, k = 6
Output: 9
Explanation: 34 (base 10) expressed in base 6 is 54. 5 + 4 = 9.
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        res = 0
        while n!=0:
            res += n%k
            n //= k
        return res
