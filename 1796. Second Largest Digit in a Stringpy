'''
https://leetcode.com/problems/second-largest-digit-in-a-string/
Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.
An alphanumeric string is a string consisting of lowercase English letters and digits.

Example 1:
Input: s = "dfa12321afd"
Output: 2
Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def secondHighest(self, s: str) -> int:
        fir = sec = -1
        for ch in s:
            if ch.isdigit():
                num = int(ch)
                if num > fir:
                    fir, sec = num, fir
                elif num == fir:
                    continue
                elif num>sec:
                    sec = num
        return sec
