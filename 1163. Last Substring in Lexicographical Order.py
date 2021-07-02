'''
https://leetcode.com/problems/last-substring-in-lexicographical-order/
Given a string s, return the last substring of s in lexicographical order.

Example 1:
Input: s = "abab"
Output: "bab"
Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def lastSubstring(self, s: str) -> str:
        i, j, diff = 0, 1, 0
        while i+diff<len(s) and j+diff<len(s):
            if s[i+diff]==s[j+diff]:
                diff += 1
            else:
                if s[i+diff]>s[j+diff]:
                    j += diff+1
                else:
                    i += diff+1
                if i==j:
                    j = i+1
                diff = 0
        return s[i:]
