'''
https://leetcode.com/problems/median-of-two-sorted-arrays/
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
'''
'''
Time:O(nlgn)
Space:O(n)
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = sorted(nums1 + nums2)
        length = len(num)
        if length%2 == 1:
            return num[length//2]
        else:
            return (num[length//2] + num[length//2-1])/2
