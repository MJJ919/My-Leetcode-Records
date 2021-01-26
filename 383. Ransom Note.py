'''
https://leetcode.com/problems/ransom-note/
Given an arbitrary ransom note string and another string containing letters from all the magazines, 
write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
'''

'''
Method below uses hashtable.
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = defaultdict(int)
        for i in magazine:
            d[i] += 1
        for i in ransomNote:
            if i not in d or d[i]==0:
                return False
            else:
                d[i] -= 1
        return True                
        
'''
Time:O(m*n)
Space:O(m)
'''
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for c in ransomNote:
            if c not in magazine:
                return False
            else:
                i = magazine.index(c)
                magazine = magazine[:i]+magazine[i+1:]
        return True
