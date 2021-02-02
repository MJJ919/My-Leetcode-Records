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
        seen = defaultdict(int)
        res = 0
        i, j = 0, 0
        while j<len(s):
            seen[s[j]] = j
            if len(seen)>2:
                del_idx = min(seen.values())
                del seen[s[del_idx]]
                i = del_idx+1
            res = max(res, j-i+1)
            j += 1
        return res
