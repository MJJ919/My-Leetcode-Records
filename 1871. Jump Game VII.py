'''
https://leetcode.com/problems/jump-game-vii/
You are given a 0-indexed binary string s and two integers minJump and maxJump. 
In the beginning, you are standing at index 0, which is equal to '0'. 
You can move from index i to index j if the following conditions are fulfilled:

i + minJump <= j <= min(i + maxJump, s.length - 1), and
s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.

Example 1:
Input: s = "011010", minJump = 2, maxJump = 3
Output: true
Explanation:
In the first step, move from index 0 to index 3. 
In the second step, move from index 3 to index 5.
'''
'''
Time:O(nlgn)
Space:O(n)
'''
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1]=='1':
            return False
        pos = []
        for idx in range(1, len(s)):
            if s[idx]=='0':
                pos.append(idx)
        p = [0]
        for num in pos:
            while p and num-p[0]>maxJump:   heapq.heappop(p)
            if p and num-p[0]>=minJump:
                heapq.heappush(p, num)
                if num==pos[-1]:
                    return True
        return False
