'''
https://leetcode.com/problems/bulls-and-cows/
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. 
Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.
The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. 
Note that both secret and guess may contain duplicate digits.
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a, b = 0, 0
        ds = defaultdict(int)
        dg = defaultdict(int)
        for i in secret:
            ds[i] += 1
        for i in guess:
            dg[i] += 1
        for j in ds:
            if j in dg:
                b += min(ds[j], dg[j])
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                a += 1
                b -= 1
        return str(a)+'A'+str(b)+'B'
