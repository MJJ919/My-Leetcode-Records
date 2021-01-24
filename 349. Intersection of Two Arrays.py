'''
https://leetcode.com/problems/intersection-of-two-arrays/submissions/
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
'''
'''
Method below uses 2 sets.
O(M+N) Time(Ave)  O(M*N) Time(Worst)
O(M+N) Space
'''
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1, nums2=sorted(set(nums1)), sorted(set(nums2))
        a = []
        for i in nums1:
            if i in nums2:
                a.append(i)
        return a 
    
'''
Method below uses 2 pointers.
Time:O(nlgn)
Space:O(n)
'''
class Solution(object):
    def intersection(self, nums1, nums2):
        nums1, nums2=sorted(set(nums1)), sorted(set(nums2))
        a = []
        i = j = 0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                i += 1
            elif nums1[i]>nums2[j]:
                j += 1
            else:
                a.append(nums1[i])
                i += 1
                j += 1
        return a 
  
'''
Method below uses python build-in function &.
Time:O(M+N)  O(M*N) Time(Worst)
space:O(M+N)
'''
class Solution(object):
    def intersection(self, nums1, nums2):
        nums1, nums2=set(sorted(nums1)), set(sorted(nums2))
        return (nums1 & nums2)
