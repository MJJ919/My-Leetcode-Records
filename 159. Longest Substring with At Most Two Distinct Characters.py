'''
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:
Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.

Example 2:
Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s)<3:
            return len(s)
        d = dict()
        res = 0
        left = 0
        for i in range(len(s)):
            char = s[i]
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
            while len(d)>2:
                d[s[left]] -= 1
                if d[s[left]]==0:
                    del d[s[left]]
                left += 1
            res = max(res, i-left+1)
        return res
