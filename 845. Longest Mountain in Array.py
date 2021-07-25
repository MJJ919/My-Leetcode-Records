'''
https://leetcode.com/problems/longest-mountain-in-array/
You may recall that an array arr is a mountain array if and only if:
arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.

Example 1:
Input: arr = [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        res = 0
        left = 0
        while left<len(arr):
            right = left
            if right+1<len(arr) and arr[right+1]>arr[right]:
                while right+1<len(arr) and arr[right+1]>arr[right]:
                    right += 1
                if right+1<len(arr) and arr[right+1]<arr[right]:
                    while right+1<len(arr) and arr[right+1]<arr[right]:
                        right += 1
                    res = max(res, right-left+1)
            left = max(left+1, right)
        return res
