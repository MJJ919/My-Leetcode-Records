'''
https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/
You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.
The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.
Return the minimum number of operations needed to make s alternating.

Example 1:
Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def minOperations(self, s: str) -> int:
        res = sum(int(ch)==(i%2) for i ,ch in enumerate(s))
        return min(res, len(s)-res)
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        s1 = '10'*(n//2)+'1'*(n%2)
        s2 = '01'*(n//2)+'0'*(n%2)
        res1, res2 = 0, 0
        for i in range(n):
            if s1[i]!=s[i]:
                res1 += 1
            if s2[i]!=s[i]:
                res2 += 1
        return min(res1, res2)
