'''
https://leetcode.com/problems/jump-game-iv/
Given an array of integers arr, you are initially positioned at the first index of the array.
In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.
Notice that you can not jump outside of the array at any time.

Example 1:
Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        visited = [False for _ in range(n)]
        d = defaultdict(set)
        for idx, ch in enumerate(arr):
            d[ch].add(idx)
        q = deque()
        q.append(0)
        step = 0
        
        while q:
            size = len(q)
            for _ in range(size):
                idx = q.popleft()
                if idx == n-1:
                    return step
                visited[idx] = True
                neighbor = set()
                for i in d[arr[idx]]:
                    if not visited[i]:
                        q.append(i)
                if idx>0 and not visited[idx-1]:
                    q.append(idx-1)
                if idx<n-1 and not visited[idx+1]:
                    q.append(idx+1)
                del d[arr[idx]]
            step += 1
