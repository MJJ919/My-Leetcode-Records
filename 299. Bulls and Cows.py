'''
https://leetcode.com/problems/bulls-and-cows/
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. 
Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.
The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        a = collections.Counter(secret)
        cow, bull=0,0
        for i,ch in enumerate(guess):
            if ch in a:
                if ch == secret[i]:
                    bull += 1
                    cow -= int(a[ch]<=0)
                else:
                    cow += int(a[ch]>0)
            a[ch] -= 1
        return "{}A{}B".format(bull,cow)
