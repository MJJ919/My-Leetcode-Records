'''
https://leetcode.com/problems/boats-to-save-people/
You are given an array people where people[i] is the weight of the ith person, 
and an infinite number of boats where each boat can carry a maximum weight of limit. 
Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
Return the minimum number of boats to carry every given person.

Example 1:
Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
'''
'''
Time:O(nlgn)
Space:O(1)
'''
class Solution:
    def numRescueBoats(self, p: List[int], limit: int) -> int:
        p.sort()
        i, j = 0, len(p)-1
        res = 0
        while i<=j:
            if p[i]+p[j]<=limit:
                res += 1
                i, j = i+1, j-1
            else:
                res += 1
                j -= 1
        return res
