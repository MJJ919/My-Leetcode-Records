'''
https://leetcode.com/problems/add-binary/
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
'''
'''
Time:O(m+n)
Space:O(1)
'''
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1=int(a,2)
        b1=int(b,2)
        out = bin(a1+b1)
        return out[2:]
    
'''
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def addBinary(self, a, b):
        a,b = a[::-1], b[::-1]
        num1, num2 = 0, 0
        for i, ch in enumerate(a):
            if ch == '1':
                num1 += 2**i
        for i, ch in enumerate(b):
            if ch == '1':
                num2 += 2**i
        num = num1 + num2
        res = []
        while num != 0:
            res.append(num%2)
            num = num//2
        return '0' if not res else ''.join(str(i) for i in res[::-1])

'''
Time:O(max(N,M))
Space:O(max(N,M))
'''
class Solution(object):
    def addBinary(self, a, b):
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        carry, res = 0, []
        for i in range(n-1, -1, -1):
            if a[i] == '1': carry += 1
            if b[i] == '1': carry += 1
            if carry%2 == 1:    res.append('1')
            else:   res.append('0')
            carry = carry//2
        if carry == 1:  res.append('1')
        res.reverse()
        return ''.join(res)
