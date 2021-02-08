'''
https://leetcode.com/problems/word-break/
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
'''
'''
Time:O(n**3)
Space:O(n)
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        words = set(wordDict)
        for i in range(1, len(s)+1):
            for j in range(i+1):
                if dp[j]==True and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[len(s)]
    
'''
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache
        def wordbreak(start):
            if start==len(s):
                return True
            for end in range(start+1, len(s)+1):
                if s[start:end] in words and wordbreak(end):
                    return True
            return False
        words = set(wordDict)
        return wordbreak(0)
