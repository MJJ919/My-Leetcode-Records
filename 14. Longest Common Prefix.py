'''
https://leetcode.com/problems/longest-common-prefix/
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
'''
'''
Method below finds the shortest string first. Then compare the shortest one with others.
Time:O(n)
Space:O(1) I guess. Not sure.
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        if len(strs) == 0:
            return prefix
        for i in range(len(min(strs))):
            c = strs[0][i]
            if all(a[i]==c for a in strs):
                prefix += c
            else:
                break
        return prefix
    
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        string = min(strs, key = len)
        for str in strs:
            i = 0
            while i<len(string):
                if string[i]!=str[i]:
                    break
                else:
                    i += 1
            string = string[:i]
            if not string:  return ""            
        return string
