'''
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
'''

'''
Method below uses dict.
'''

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {}
        for i in s:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] = dict[i]+1
        return sum(v % 2 for v in dict.values()) < 2
       
'''
Method below uses set.
'''

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        unpaired = set()
        
        for i in s:
            if i not in unpaired:
                unpaired.add(i)
            else:
                unpaired.remove(i)
        return len(unpaired) < 2
        
