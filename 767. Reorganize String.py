'''
https://leetcode.com/problems/reorganize-string/
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
Return any possible rearrangement of s or return "" if not possible.

Example 1:
Input: s = "aab"
Output: "aba"
'''
'''
'''
class Solution:
    def reorganizeString(self, s: str) -> str:
        d = Counter(s)
        q = []
        for key, value in d.items():
            heapq.heappush(q, [-value, key])
        temp_occur, temp_ch = 0, ''
        res = []
        while q:
            occur, ch = heapq.heappop(q)
            res.append(ch)
            if temp_occur<0:
                heapq.heappush(q, [temp_occur, temp_ch])
            occur += 1
            temp_occur, temp_ch = occur, ch
        return ''.join(res) if len(res)==len(s) else ''
