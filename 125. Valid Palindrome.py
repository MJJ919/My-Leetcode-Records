'''
https://leetcode.com/problems/valid-palindrome/
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = "".join([c for c in s if c.isalnum()]).lower() #isalnum() judges whether this character is a number/letter or not
        # Another method: s = re.sub('[^A-Za-z0-9]+', '', s).lower()
        return s[::-1] == s

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
