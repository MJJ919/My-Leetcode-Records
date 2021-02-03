'''
https://leetcode.com/problems/different-ways-to-add-parentheses/
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. 
The valid operators are +, - and *.

Example 1:
Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2
'''
'''
'''
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        memo = {}
        
        def helper(m, n, op):
            if op == '+':
                return m+n
            elif op == '-':
                return m-n
            else:
                return m*n
            
        if input.isdigit():
            return [int(input)]
        if input in memo:
            return memo[input] 
        res = []
        for i in range(len(input)):
            if input[i] in "-+*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for j in res1:
                    for k in res2:
                        res.append(helper(j, k, input[i]))
        memo[input] = res
        return res
