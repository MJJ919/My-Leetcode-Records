'''
https://leetcode.com/problems/ugly-number-ii/
Write a program to find the n-th ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:
Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        i, j, k = 0, 0, 0
        for _ in range(n-1):
            temp = min(res[i]*2, res[j]*3, res[k]*5)
            res.append(temp)
            if res[i]*2==temp:
                i += 1
            if res[j]*3==temp:
                j += 1
            if res[k]*5==temp:
                k += 1
        return res[-1]
