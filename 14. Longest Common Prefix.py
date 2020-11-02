'''

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
        if not strs:
            return ""
        shortest = min(strs,key=len) 
        #find the shortest string in the list by usng min(key)
        for i, ch in enumerate(shortest):
            for str in strs:
                if str[i] != ch:
                    return shortest[:i]
        return shortest
