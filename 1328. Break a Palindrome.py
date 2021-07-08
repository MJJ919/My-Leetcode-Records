'''
https://leetcode.com/problems/break-a-palindrome/
Given a palindromic string of lowercase English letters palindrome, replace exactly one character 
with any lowercase English letter so that the resulting string is not a palindrome and that 
it is the lexicographically smallest one possible.

Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position 
where a and b differ, a has a character strictly smaller than the corresponding character in b. 
For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character, 
and 'c' is smaller than 'd'.

Example 1:
Input: palindrome = "abccba"
Output: "aaccba"
Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def breakPalindrome(self, p: str) -> str:
        if len(p) == 1:
            return ''
        for i in range(len(p)//2):
            if p[i]!='a':
                return p[:i]+'a'+p[i+1:]
        return p[:-1]+'b'
