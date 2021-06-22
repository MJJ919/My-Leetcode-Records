'''
https://leetcode.com/problems/number-of-matching-subsequences/
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.
A subsequence of a string is a new string generated from the original string with some characters 
(can be none) deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".
 
Example 1:
Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
'''
'''
Time:O(len(s)+S(len(word for word in words)))
Space:O(n)
'''
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        res = 0
        d = [[] for _ in range(26)]
        for word in words:
            d[ord(word[0])-ord('a')].append(word)
        
        for ch in s:
            idx = ord(ch)-ord('a')
            old = d[idx]
            d[idx] = []
            while old:
                word = old.pop()
                if len(word)==1:
                    res += 1
                else:
                    d[ord(word[1])-ord('a')].append(word[1:])
        return res
