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
                     
