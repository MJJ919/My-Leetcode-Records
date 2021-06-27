'''
https://leetcode.com/problems/jump-game-v/
Given an array of integers arr and an integer d. In one step you can jump from index i to index:

i + x where: i + x < arr.length and 0 < x <= d.
i - x where: i - x >= 0 and 0 < x <= d.
In addition, you can only jump from index i to index j if arr[i] > arr[j] and arr[i] > arr[k] 
for all indices k between i and j (More formally min(i, j) < k < max(i, j)).

You can choose any index of the array and start jumping. Return the maximum number of indices you can visit.
Notice that you can not jump outside of the array at any time.

Example 1:
Input: arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
Output: 4
Explanation: You can start at index 10. You can jump 10 --> 8 --> 6 --> 7 as shown.
Note that if you start at index 6 you can only jump to index 7. You cannot jump to index 5 because 13 > 9. You cannot jump to index 4 because index 5 is between index 4 and 6 and 13 > 9.
Similarly You cannot jump from index 3 to index 2 or index 1.
'''
'''
Time:O(n*n)
Space:O(n)
'''
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        memo = [0 for _ in range(n)]
        
        def dfs(i):
            if memo[i]>0:   return memo[i]
            res = 1
            for j in range(i+1, min(i+d, n-1)+1):
                if arr[j]>=arr[i]:
                    break
                res = max(res, 1+dfs(j))
            for j in range(i-1, max(0, i-d)-1, -1):
                if arr[j]>=arr[i]:
                    break
                res = max(res, 1+dfs(j))
            memo[i] = res
            return memo[i]
        
        for i in range(n):
            dfs(i)
        return max(memo)
