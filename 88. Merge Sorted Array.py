'''
https://leetcode.com/problems/merge-sorted-array/solution/
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m-1, n-1
        for p in range(m+n-1, -1, -1):
            if j<0:
                break
            if nums1[i]>nums2[j] and i>= 0:
                nums1[p] = nums1[i]
                i -= 1
            else:
                nums1[p] = nums2[j]
                j -= 1
            
'''
Time:O(nlgn)
Spaec:O(n)
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[m:] = nums2
        return nums1.sort()
