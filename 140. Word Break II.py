'''
https://leetcode.com/problems/word-break-ii/
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def back(s, res, memo):
            if s in memo:
                return memo[s]
            if not s:
                return
            res = []
            for word in wordDict:
                if not s.startswith(word):
                    continue
                if len(word)==len(s):
                    res.append(word)
                else:
                    rest = back(s[len(word):], res, memo)
                    for i in rest:
                        segment = word+' '+i
                        res.append(segment)
                        
            memo[s] = res
            return res
        
        return back(s, [], {})
