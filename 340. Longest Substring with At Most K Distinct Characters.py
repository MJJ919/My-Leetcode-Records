'''
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

Example 1:
Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
'''
'''
Time:O(n)
Space:O(len(s))
'''
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        seen = defaultdict(int)
        i, j = 0, 0
        res = 0
        while j<len(s):
            seen[s[j]] = j
            if len(seen)>k:
                idx = min(seen.values())
                del seen[s[idx]]
                i = idx+1
            res = max(res, j-i+1)
            j += 1
        return res
