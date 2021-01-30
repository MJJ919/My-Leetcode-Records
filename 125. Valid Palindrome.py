'''
https://leetcode.com/problems/valid-palindrome/
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(i.lower() for i in s if i.isalnum())
        return s==s[::-1]

'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def isPalindrome(self, s):
        s = re.sub('[^A-Za-z0-9]+', '', s).lower()
        i, j = 0, len(s)-1
        while i<j:
            if s[i] != s[j]:    
                return False
            i, j = i+1, j-1
        return True
