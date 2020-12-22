'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

'''
Method below uses sliding window.
Time:O(n)
Space:O(m)
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        i, res = 0, 0
        for j in range(len(s)):
            if s[j] in d:
                i = max(d[s[j]],i)
            res = max(res, j-i+1)
            d[s[j]] = j+1
        return res
