'''
https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = {}
        for pair in knowledge:
            d[pair[0]] = pair[1]
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
