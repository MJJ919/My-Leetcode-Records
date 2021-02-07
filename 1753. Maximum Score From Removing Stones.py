'''
https://leetcode.com/problems/maximum-score-from-removing-stones/
You are playing a solitaire game with three piles of stones of sizes a, b, and c respectively. 
Each turn you choose two different non-empty piles, take one stone from each, and add 1 point to your score. 
The game stops when there are fewer than two non-empty piles (meaning there are no more available moves).

Given three integers a, b, and c, return the maximum score you can get.
'''
'''
Time:O(1)
Space:O(1)
'''
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        return min((a+b+c)//2, (a+b+c)-max(a,b,c))
