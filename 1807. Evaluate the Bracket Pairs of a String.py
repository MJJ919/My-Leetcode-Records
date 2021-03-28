'''
https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = {key:value for key, value in knowledge}
        scan = ''
        res = ''
        flag = False
        for letter in s:
            if letter == '(':
                flag = True
            elif letter == ')':
                if scan in d:
                    res += d[scan]
                else:
                    res += '?'
                scan = ''
                flag = False
            else:
                if flag:
                    scan += letter
                else:
                    res += letter
        return res
