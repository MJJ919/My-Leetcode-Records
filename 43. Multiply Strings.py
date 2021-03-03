'''
https://leetcode.com/problems/multiply-strings/
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"
'''
'''
Time:O(n**2)
Space:O(1)
'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n = len(num1)+len(num2)
        res = [0 for _ in range(n)]
        for idx1, ch1 in enumerate(reversed(num1)):
            for idx2, ch2 in enumerate(reversed(num2)):
                idx = n-1-idx1-idx2
                res[idx] += int(ch1)*int(ch2)
                res[idx-1] += res[idx]//10
                res[idx] = res[idx]%10
        a = 0
        while a<len(res)-1 and res[a]==0:
            a += 1
        return ''.join(str(i) for i in res[a:])
