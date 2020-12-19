'''
https://leetcode.com/problems/first-unique-character-in-a-string/
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
'''

'''
Method below uses hashtable.
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        for i,ch in enumerate(s):
            if d[ch]==1:
                return i
        return -1
