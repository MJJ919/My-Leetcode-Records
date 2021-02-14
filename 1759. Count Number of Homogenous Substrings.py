'''
https://leetcode.com/problems/count-number-of-homogenous-substrings/
Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 109 + 7.
A string is homogenous if all the characters of the string are the same.
A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "abbcccaa"
Output: 13
Explanation: The homogenous substrings are listed as below:
"a"   appears 3 times.
"aa"  appears 1 time.
"b"   appears 2 times.
"bb"  appears 1 time.
"c"   appears 3 times.
"cc"  appears 2 times.
"ccc" appears 1 time.
3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.
'''
class Solution:
    def countHomogenous(self, s: str) -> int:
        if not s:
            return 0
        i, j = 0, 0
        res = 0
        while j<len(s):
            while j<len(s) and s[i]==s[j]:
                j += 1
            length = j-i
            n = 0
            for num in range(1, length+1):
                n += num
            res += n
            i = j
        return mod(res, 10**9+7)
