'''
https://leetcode.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/
You are given two strings a and b that consist of lowercase letters. In one operation, you can change any character in a or b to any lowercase letter.
Your goal is to satisfy one of the following three conditions:

Every letter in a is strictly less than every letter in b in the alphabet.
Every letter in b is strictly less than every letter in a in the alphabet.
Both a and b consist of only one distinct letter.
Return the minimum number of operations needed to achieve your goal.
'''
'''
Time:O(n)
Space:O(26)
'''
class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        m, n = len(a), len(b)
        c1, c2 = Counter(ord(i)-97 for i in a), Counter(ord(j)-97 for j in b)
        res = m+n-max((c1+c2).values())
        for i in range(25):
            c1[i+1] += c1[i]
            c2[i+1] += c2[i]
            res = min(m-c1[i]+c2[i], res)
            res = min(n-c2[i]+c1[i], res)
        return res
