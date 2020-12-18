'''
https://leetcode.com/problems/intersection-of-two-arrays-ii/
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
'''

'''
Method below uses 2 pointers.
Time:O(nlogn)
Space:O(1)
'''
class Solution(object):
    def intersect(self, nums1, nums2):
        nums1, nums2 = sorted(nums1), sorted(nums2)
        i = j = 0 
        a=[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                i = i+1
            elif nums1[i]>nums2[j]:
                j = j+1
            else:
                a.append(nums1[i])
                i,j = i+1, j+1
        return a 


'''
Method below uses hashmap.
Time: O(n)
Space: O(min(n,m))
'''
class Solution(object):
    def intersect(self, nums1, nums2):
        nums1, nums2 = sorted(nums1), sorted(nums2)
        a = {}
        res = []
        for i in nums1:
            if not a.has_key(i):
                a[i] = 1
            else:
                a[i] += 1
        for i in nums2:
            if a.has_key(i) and a[i]!=0:
                res.append(i)
                a[i] -= 1
        return res
        
'''
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def intersect(self, nums1, nums2):
        a = collections.Counter(nums1)
        res = []
        for num in nums2:
            if num in a and a[num] >0:
                res.append(num)    
                a[num] -= 1
        return res
