'''
https://leetcode.com/problems/remove-duplicate-letters/
Given a string s, remove duplicate letters so that every letter appears once and only once. 
You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:
Input: s = "bcabc"
Output: "abc"
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d = {ch:idx for idx, ch in enumerate(s)}
        res = deque()
        seen = set()
        for idx, ch in enumerate(s):
            if ch not in seen:
                while res and ch<res[-1] and d[res[-1]]>idx:
                    seen.remove(res.pop())
                res.append(ch)
                seen.add(ch)
        return ''.join(res)
