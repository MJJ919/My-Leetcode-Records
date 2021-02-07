'''
https://leetcode.com/problems/minimum-window-substring/
Given two strings s and t, return the minimum window in s which will contain all the characters in t. 
If there is no such window in s that covers all characters in t, return the empty string "".
Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
'''
'''
Space: O(|S| + |T|)
Time: O(|S| + |T|)
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:  return ''
        dict_t = Counter(t)
        len_t = len(dict_t)
        dict_s, seen = defaultdict(int), 0
        res = [float('inf'), 0, 0]
        i, j = 0, 0
        while j<len(s):
            ch = s[j]
            dict_s[ch] += 1
            if ch in dict_t and dict_t[ch]==dict_s[ch]:
                seen += 1
            while i<=j and seen==len_t:
                ch = s[i]
                dict_s[ch] -= 1
                if j-i+1 < res[0]:
                    res = [j-i+1, i, j]
                if ch in dict_t and dict_s[ch]<dict_t[ch]:
                    seen -= 1
                i += 1
            j += 1
        return '' if res[0]==float('inf') else s[res[1]:res[2]+1]
