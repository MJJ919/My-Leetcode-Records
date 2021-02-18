'''
https://leetcode.com/problems/perfect-number/
A perfect number is a positive integer that is equal to the sum of its positive divisors, 
excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise return false.

Example 1:
Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.
'''
'''
Time:O(sqrt(n))
Space:O(1)
'''
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        s = 0
        i = 1
        while i*i<=num:
            if num%i==0:
                s += i
                if i*i != num:
                    s += num//i
            i += 1
        return s ==2*num
