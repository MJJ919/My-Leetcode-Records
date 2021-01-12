'''
https://leetcode.com/problems/super-ugly-number/description/
Write a program to find the nth super ugly number.
Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

Example:
Input: n = 12, primes = [2,7,13,19]
Output: 32 
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
             super ugly numbers given primes = [2,7,13,19] of size 4.
'''
'''
'''
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        s, h = set([1]), [1]
        while n:
            i = heappop(h)
            for j in primes:
                num = i*j
                if num not in s:
                    heappush(h, num)
                    s.add(num)
            n -= 1
        return i
