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
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<3:    return len(s)
        left, right = 0, 0
        mx = 2
        d = defaultdict(int)
        while right<len(s):
            d[s[right]] = right
            right += 1
            if len(d) == 3:
                idx = min(d.values())
                del d[s[idx]]
                left = idx+1
            mx = max(mx, right-left)
        return mx
