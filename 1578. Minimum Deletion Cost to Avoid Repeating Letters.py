'''
https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/
Given a string s and an array of integers cost where cost[i] is the cost of deleting the ith character in s.
Return the minimum cost of deletions such that there are no two identical letters next to each other.
Notice that you will delete the chosen characters at the same time, in other words, after deleting a character, 
the costs of deleting other characters will not change.

Example 1:
Input: s = "abaac", cost = [1,2,3,4,5]
Output: 3
Explanation: Delete the letter "a" with cost 3 to get "abac" (String without two identical letters next to each other).
'''
'''
'''
lass Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        if len(s)==1:   return 0
        total, maxcost = 0, 0
        res = 0
        for i in range(len(s)):
            if i>0 and s[i-1]!=s[i]:
                res += total - maxcost
                maxcost = 0
                total = 0
            maxcost = max(maxcost, cost[i])
            total += cost[i]
        res += total - maxcost
        return res
