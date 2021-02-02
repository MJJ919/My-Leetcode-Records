'''
https://leetcode.com/problems/valid-parentheses/description/
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.Open brackets must be closed in the correct order.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
'''
'''
Method below uses stack.
Time=O(n)
Space=O(n)
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {')':'(', ']':'[', '}':'{'}
        stack = []
        for i in s:
            if i in d.values():
                stack.append(i)
            elif stack and d[i] == stack[-1]:
                    del stack[-1]
            else:
                return False
        return not stack

class Solution:
    def isValid(self, s: str) -> bool:
        pair = {')':'(', '}':'{', ']':'['}
        stack = deque()
        for i in s:
            if i not in pair:
                stack.append(i)
            elif not stack or stack.pop() != pair[i]:
                return False
        if not stack:
            return True
        return False
