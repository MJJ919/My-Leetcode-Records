'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
Return the answer in any order.
'''
'''
Time=O[(3**n)*(4**m)]
Spcae=O[(3**n)*(4**m)]
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}
        def back(digits, cur):
            if len(digits)==0:
                res.append(cur[:])
                return 
            for i in d[digits[0]]:
                cur += i
                back(digits[1:], cur)
                cur = cur[:-1]
        
        res =[]
        if digits:
            back(digits, '')
        return res
