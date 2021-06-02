'''
https://leetcode.com/problems/longest-repeating-character-replacement/
You are given a string s and an integer k. 
You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
'''
'''
Time:O(n*n)
Space:O(n)
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        left = 0
        count = [0 for _ in range(26)]
        for i in range(len(s)):
            c = s[i]
            count[ord(c)-65] += 1
            while i-left+1-max(count)>k:
                l = s[left]
                left += 1
                count[ord(l)-65] -= 1
            res = max(res, i-left+1)
        return res
