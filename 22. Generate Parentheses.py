'''
https://leetcode.com/problems/generate-parentheses/
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
'''
'''
Time:
Space:
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(bracket, left, right):
            if len(bracket)==2*n:
                res.append(bracket)
            if left<n:
                dfs(bracket+'(', left+1, right)
            if right<left:
                dfs(bracket+')', left, right+1)
        dfs('', 0, 0)
        return res
