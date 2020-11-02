'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

'''

'''
Time=O[(3**n)*(4**m)]
Spcae=O[(3**n)*(4**m)]
'''
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        map={'2': ['a', 'b', 'c'],'3': ['d', 'e', 'f'],'4': ['g', 'h', 'i'],'5': ['j', 'k', 'l'],'6': ['m', 'n', 'o'],'7': ['p', 'q', 'r', 's'],'8': ['t', 'u', 'v'],'9': ['w', 'x', 'y', 'z']}
        
        def find(combine, next_dig):
            if not next_dig:
                output.append(combine)
            else:
                for letter in map[next_dig[0]]:
                    find(combine+letter, next_dig[1:])
        output=[]    
        if digits:
            find('',digits)
        return output
