'''
https://leetcode.com/problems/matchsticks-to-square/
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick.
You want to use all the matchsticks to make one square. You should not break any stick, 
but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

Example 1:
Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
'''
'''
Time:O(4^n)
Space:O(n)
'''
class Solution:
    def makesquare(self, m: List[int]) -> bool:
        if sum(m)%4 != 0:
            return False
        length = sum(m)//4
        if any(i>length for i in m):
            return False
        m.sort(reverse = True)
        s = [0 for _ in range(4)]
        
        def find(start):
            if start == len(m):
                return s[0]==s[1]==s[2]==s[3]==length
            for i in range(4):
                if m[start]+s[i]<=length:
                    s[i] += m[start]
                    if find(start+1):
                        return True
                    s[i] -= m[start]
            return False
        
        return find(0)            
