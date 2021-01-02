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
Time:
Space:
'''
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        product = [0]*(len(num1)+len(num2))
        pos = len(product)-1
        for i in reversed(num1):
            p = pos
            for j in reversed(num2):
                product[p] += int(i)*int(j)
                product[p-1] += product[p]/10
                product[p] = product[p]%10
                p -= 1
            pos -= 1
        a = 0
        while a<len(product)-1 and product[a]==0:
                a += 1 
        return ''.join(str(i) for i in product[a:])
