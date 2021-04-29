'''
https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/
A string is considered beautiful if it satisfies the following conditions:
Each of the 5 English vowels ('a', 'e', 'i', 'o', 'u') must appear at least once in it.
The letters must be sorted in alphabetical order (i.e. all 'a's before 'e's, all 'e's before 'i's, etc.).
For example, strings "aeiou" and "aaaaaaeiiiioou" are considered beautiful, but "uaeio", "aeoiu", and "aaaeeeooo" are not beautiful.

Example 1:
Input: word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
Output: 13
Explanation: The longest beautiful substring in word is "aaaaeiiiiouuu" of length 13.
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        res = 0
        s = set()
        i = 0
        for j in range(len(word)):
            s.add(word[j])
            if j > i:
                if ord(word[j]) >= ord(word[j - 1]):
                    if len(s) == 5:
                        res = max(res, j - i + 1)
                else:
                    if j!= len(word)-1:
                        s = set(word[j])
                        i = j
        return res
