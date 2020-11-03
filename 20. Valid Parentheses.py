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
        mapping = {"}":"{", ")":"(", "]":"["}
        stack = []
        if len(s)%2 == 1:
            return False #if the len of s is odd then the result must be F
        else:
            for char in s:
                if char in mapping.values():
                    stack.append(char)
                elif char in mapping:
                        if stack == [] or mapping[char] != stack.pop():
                            return False
        return stack==[]
                     
