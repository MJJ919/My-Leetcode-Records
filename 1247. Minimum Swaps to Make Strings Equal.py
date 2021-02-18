'''
https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/
You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only. 
Your task is to make these two strings equal to each other. 

You can swap any two characters that belong to different strings, which means: swap s1[i] and s2[j].
Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.

Example 1:
Input: s1 = "xx", s2 = "yy"
Output: 1
Explanation: 
Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x, y = 0, 0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                if s1[i]=='x':
                    x += 1
                else:
                    y += 1
        if (x+y)%2 == 1:
            return -1
        return x//2 + y//2 + x%2 + y%2
