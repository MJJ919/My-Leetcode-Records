'''
https://leetcode.com/problems/jump-game-iii/
Given an array of non-negative integers arr, you are initially positioned at start index of the array. 
When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.
Notice that you can not jump outside of the array at any time.

Example 1:
Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        s = [start]
        while s:
            node = s.pop(0)
            if arr[node]==0:    return True
            if arr[node]<0: continue
            for i in [node-arr[node], node+arr[node]]:
                if n>i>=0:
                    s.append(i)
            arr[node] = -arr[node]
        return False
        
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if len(arr)>start>=0 and arr[start]>=0:
            if arr[start]==0:   return True
            
            arr[start] = -arr[start]
            return self.canReach(arr, start+arr[start]) or self.canReach(arr, start-arr[start])
        return False
