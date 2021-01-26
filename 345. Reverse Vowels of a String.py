'''
https://leetcode.com/problems/reverse-vowels-of-a-string/
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Input: "hello"
Output: "holle"

Example 2:
Input: "leetcode"
Output: "leotcede"
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i, j = 0, len(s)-1
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        while i <= j:
            while i<j and s[i] not in vowel:
                i += 1
            while i<j and s[j] not in vowel:
                j -= 1
            s[i], s[j] = s[j], s[i]
            i, j = i+1, j-1
        return ''.join(s)
