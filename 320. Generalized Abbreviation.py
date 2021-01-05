'''
https://leetcode.com/problems/generalized-abbreviation/
A word's generalized abbreviation can be constructed by taking any number of non-overlapping substrings and replacing them with their respective lengths. 
For example, "abcde" can be abbreviated into "a3e" ("bcd" turned into "3"), "1bcd1" ("a" and "e" both turned into "1"), and "23" ("ab" turned into "2" and "cde" turned into "3").

Given a string word, return a list of all the possible generalized abbreviations of word. Return the answer in any order.

Example 1:
Input: word = "word"
Output: ["4","3d","2r1","2rd","1o2","1o1d","1or1","1ord","w3","w2d","w1r1","w1rd","wo2","wo1d","wor1","word"]
'''

class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        n = len(word)
        res = []
        def back(idx, cur):
            if idx == n:
                res.append(cur)
                return 
            back(idx+1, cur+word[idx])
            for i in range(1, n-idx+1):
                if not cur or not cur[-1].isnumeric():
                    back(idx+i, cur+str(i))
                else:   return
        back(0, '')
        return res
