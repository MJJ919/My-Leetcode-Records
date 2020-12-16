'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
'''

'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m-1, n-1, m+n-1
        while i>=0 and j>=0:
            if nums1[i]>=nums2[j]:
                nums1[k] = nums1[i]
                i, k = i-1, k-1
            else:
                nums1[k] = nums2[j]
                j,k = j-1, k-1
        nums1[:j+1] = nums2[:j+1]
        return nums1
            
'''
Time:O(nlgn)
Spaec:O(n)
'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[m:] = nums2
        return nums1.sort()
