'''
https://leetcode.com/problems/frog-jump/
A frog is crossing a river. The river is divided into some number of units, and at each unit, 
there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, 
determine if the frog can cross the river by landing on the last stone. 
Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. 
The frog can only jump in the forward direction.

Example 1:
Input: stones = [0,1,3,5,6,8,12,17]
Output: true
Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, 
then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 
4 units to the 7th stone, and 5 units to the 8th stone.
'''
'''
Time:O(n^2)
Space:O(n^2)
'''
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        d = {}
        for s in stones:
            d[s] = set()
        d[0].add(1)
        last = stones[-1]
        for pos in stones:
            for size in d[pos]:
                nextpos = size+pos
                if nextpos == last:
                    return True
                if nextpos in d:
                    d[nextpos].add(size)
                    d[nextpos].add(size+1)
                    if size>1:
                        d[nextpos].add(size-1)
        return False
        
'''
Time:O(n^3)
Space:O(n^2)
'''
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        memo = [[-1 for _ in range(n)]for _ in range(n)]
        def jump(size, pos):
            if memo[pos][size] != -1:
                return memo[pos][size]
            for i in range(pos+1, n):
                gap = stones[i]-stones[pos]
                if size+1>=gap>=size-1:
                    if jump(gap, i):
                        memo[i][gap] = 1
                        return memo[i][gap]
            memo[pos][size] = 1 if pos==n-1 else 0
            return memo[pos][size]
        
        return jump(0,0)
