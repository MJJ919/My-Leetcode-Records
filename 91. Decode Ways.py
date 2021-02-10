'''
https://leetcode.com/problems/decode-ways/
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be mapped back into letters using the reverse of the mapping above (there may be multiple ways). 
Given a non-empty string num containing only digits, return the number of ways to decode it.
The answer is guaranteed to fit in a 32-bit integer.

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s)+1)]
        dp[0]=1
        dp[1]=1 if s[0]!='0' else 0
        for i in range(2, len(s)+1):
            if s[i-1]!='0':
                dp[i] += dp[i-1]
            num = int(s[i-2:i])
            if num>=10 and num<=26:
                dp[i] += dp[i-2]
        return dp[-1]
                
