'''
https://leetcode.com/problems/reverse-words-in-a-string/
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(reversed(s.split()))
        
'''
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def reverseWords(self, s):
        i, j = 0, len(s)-1
        while i<=j and s[i] == ' ':
            i += 1
        while i<=j and s[j] == ' ':
            j -= 1
        
        word, d = [], deque()
        while i<=j:
            if s[i] != ' ':
                word.append(s[i])
            elif s[i] == ' ' and word:
                d.appendleft(''.join(word))
                word = []
            i += 1
        d.appendleft(''.join(word))
        return ' '.join(d)
