'''
https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
Return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.
Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/

Example 1:
Input: s = "bcabc"
Output: "abc"
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        idx = {ch:i for i, ch in enumerate(s)}
        seen = set()
        res = deque()
        for i in range(len(s)):
            ch = s[i]
            if ch not in seen:
                seen.add(ch)
                while res and res[-1]>ch and i<idx[res[-1]]:
                        seen.remove(res.pop())
                res.append(ch)
        return ''.join(res)
