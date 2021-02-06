'''
https://leetcode.com/problems/palindrome-pairs/
Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, 
so that the concatenation of the two words words[i] + words[j] is a palindrome.

Example 1:
Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
'''
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        dict = {word:idx for idx, word in enumerate(words)}
        res = []
        def valid_prefix(word):
            prefix = []
            for i in range(len(word)):
                if word[:i+1]==word[:i+1][::-1]:
                    prefix.append(word[i+1:])
            return prefix
        
        def valid_suffix(word):
            suffix = []
            for i in range(len(word)):
                if word[i:]==word[i:][::-1]:
                    suffix.append(word[:i])
            return suffix
                
        for ch, word in enumerate(words):
            rev_word = word[::-1]
            if rev_word in dict and dict[rev_word]!=ch:
                res.append([ch, dict[rev_word]])
            
            for prefix in valid_prefix(rev_word):
                if prefix in dict:
                    res.append([ch, dict[prefix]])
            
            for suffix in valid_suffix(rev_word):
                if suffix in dict:
                    res.append([dict[suffix], ch])
                    
        return res
