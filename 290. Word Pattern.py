'''
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
'''

'''
Method below uses 2 dicts.
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        dict1 ={}
        dict2 = {}
        s = s.split()
        if len(pattern) != len(s):
            return False
        for i in range(len(pattern)):
            c = pattern[i]
            w = s[i]
            if c not in dict1:
                dict1[c] = i
            if w not in dict2:
                dict2[w] = i 
            if dict1[c] != dict2[w]:
                return False
        return True

'''
Method below uses zip function.
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def wordPattern(self, pattern, s):
        p = pattern
        s = s.split()
        return len(set(zip(s, p))) == len(set(s)) == len(set(p)) and len(s) == len(p)
