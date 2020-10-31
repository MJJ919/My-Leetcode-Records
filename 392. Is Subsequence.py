'''
Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).
'''

'''
Method below uses 2 pointers, starts comparing from the right.
Time:O(∣T∣)
Space:O(1)
'''
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = len(s)-1
        j = len(t)-1
        while i>=0 and j>=0:
            if s[i]==t[j]:
                j -= 1
                i -= 1
            else:
                j -= 1
        return i==-1
            
'''
Method below uses iter() function.
Time:O(|s| + |t|)
Space:O(1)
'''
def isSubsequence(self, s, t):
    remainder_of_t = iter(t)
    for letter in s:
        if letter not in remainder_of_t:
            return False
    return True
