'''
https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/
Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

1. Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
2. Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
3. The prefix and the suffix should not intersect at any index.
4. The characters from the prefix and suffix must be the same.
5. Delete both the prefix and the suffix.
Return the minimum length of s after performing the above operation any number of times (possibly zero times).
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def minimumLength(self, s: str) -> int:
        i, j = 0, len(s)-1
        while i<j and s[i]==s[j]:
            ch = s[i]
            while i<=j and ch == s[i]:
                i += 1
            while j>=i and ch == s[j]:
                j -= 1
        return 0 if i>j else j-i+1
