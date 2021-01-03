'''
https://leetcode.com/problems/basic-calculator-ii/
Given a string s which represents an expression, evaluate this expression and return its value. 
The integer division should truncate toward zero.

Example 1:
Input: s = "3+2*2"
Output: 7

Example 2:
Input: s = " 3/2 "
Output: 1
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def calculate(self, s: str) -> int:
        cur, operator = 0, '+'
        operations = ['+', '-', '*', '/']
        stack = []
        for inx, i in enumerate(s):
            if i.isdigit():
                cur = cur*10+int(i)
            if i in operations or inx==len(s)-1:
                if operator=='+':
                    stack.append(cur)
                elif operator == '-':
                    stack.append(-cur)
                elif operator == '*':
                    stack[-1] = int(stack[-1]*cur)
                else:
                    stack[-1] = int(stack[-1]/cur)
                operator = i
                cur = 0
        return sum(stack)
