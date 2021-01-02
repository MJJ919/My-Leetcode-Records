'''
https://leetcode.com/problems/evaluate-reverse-polish-notation/
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:
Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.

Example 1:
Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
'''
'''
Time:O(n)
Space:O(n)
'''
#PY3
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            '+':lambda a, b:a+b,
            '-':lambda a, b:a-b,
            '*':lambda a, b:a*b,
            '/':lambda a, b:int(a/b)
        }
        s = []
        for i in tokens:
            if i in operations:
                b = s.pop()
                a = s.pop()
                operation = operations[i]
                s.append(operation(int(a),int(b)))
            else:
                s.append(i)
        return s.pop()
