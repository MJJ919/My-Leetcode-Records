'''
https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
Given a string s and an integer k, return the length of the longest substring of s such that 
the frequency of each character in this substring is greater than or equal to k.

Example 1:
Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:
Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
'''
'''
Time:O(n**2)
Space:O(n)
'''
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s)<k:
            return 0
        c = min(set(s), key = s.count)
        for i in c:
            if s.count(i) >= k:
                return len(s)
        return max(self.longestSubstring(t,k) for t in s.split(c))
