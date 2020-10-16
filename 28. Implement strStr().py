'''
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

'''
The following method is so pythonic.
'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
        
  
'''
The following method uses sliding window.
'''
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for start in range(len(haystack)-len(needle)+1):
            if haystack[start : start+len(needle)] == needle:
                return start
        return -1
