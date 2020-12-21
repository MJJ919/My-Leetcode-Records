'''
https://leetcode.com/problems/palindrome-permutation/
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
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        return sum(v % 2 for v in dict.values()) < 2
 
'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def canPermutePalindrome(self, s):
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        flag = 0
        for i in d:
            if d[i] != 2:
                flag += 1
            if flag > 1:
                    return False
        return True
    
'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = []
        for i in s:
            if i in l:
                l.remove(i)
            else:
                l.append(i)
        return len(l)<2
