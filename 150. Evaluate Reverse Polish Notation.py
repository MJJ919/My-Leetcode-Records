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

'''
Time:O(n**2)
Space:O(1)
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def operation(token, num1, num2):
            if token == '+':
                return num1 + num2
            elif token == '-':
                return num1 - num2
            elif token == '*':
                return num1 * num2
            else:
                return int(num1 / num2)
        cur = 0
        length = len(tokens)
        while length>1:
            while tokens[cur] not in "+-*/":
                cur += 1
            num1 = int(tokens[cur-2])
            num2 = int(tokens[cur-1])
            res = operation(tokens[cur], num1, num2)
            tokens[cur] = res
            tokens.pop(cur-1)
            tokens.pop(cur-2)
            cur -= 1
            length -= 2
        return tokens[0]
