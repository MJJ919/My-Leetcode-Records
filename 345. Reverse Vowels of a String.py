'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
'''

'''
Method below uses 2 pointers.
'''
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowel = ('AEIOUaeiou')
        i,j = 0, len(s)-1
        while i<j:
            if s[i] in vowel and s[j] in vowel:
                s[i],s[j] = s[j],s[i]
                i, j = i+1, j-1
            elif s[i] not in vowel:
                i = i+1
            else:
                j = j-1
        return ''.join(s)
