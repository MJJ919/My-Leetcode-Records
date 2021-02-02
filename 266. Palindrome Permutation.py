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
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        return sum(v % 2 for v in dict.values()) < 2
 
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)
        count = 0
        for ch in counter:
            if counter[ch]!=2:
                count += 1
        return count<2
    
class Solution(object):
    def canPermutePalindrome(self, s):
        l = []
        for i in s:
            if i in l:
                l.remove(i)
            else:
                l.append(i)
        return len(l)<2
