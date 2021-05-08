'''
https://leetcode.com/problems/put-boxes-into-the-warehouse-ii/
You are given two arrays of positive integers, boxes and warehouse, 
representing the heights of some boxes of unit width and the heights of n rooms in a warehouse respectively. 
The warehouse's rooms are labeled from 0 to n - 1 from left to right where warehouse[i] (0-indexed) is the height of the ith room.

Example 1:
Input: boxes = [1,2,2,3,4], warehouse = [3,4,1,2]
Output: 4
'''
'''
Time:O(nlgn)
Space:O(1)
'''
class Solution:
    def maxBoxesInWarehouse(self, b: List[int], w: List[int]) -> int:
        n = len(w)
        i = 0
        j = n-1
        idx = 0
        b.sort(reverse=True)
        while i<=j and idx<len(b):
            if b[idx]<=w[i]:
                i+=1
            elif b[idx]<=w[j]:
                j-=1
            idx += 1
        return i+n-1-j
