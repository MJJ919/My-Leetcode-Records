'''
https://leetcode.com/problems/median-of-two-sorted-arrays/
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
'''
'''
Time:O(lgn)
Space:O(1)
'''
class Solution:
    def findMedianSortedArrays(self, n1: List[int], n2: List[int]) -> float:
        if len(n1)>len(n2):
            return self.findMedianSortedArrays(n2, n1)
        left, right = 0, len(n1)
        while left<=right:
            x = left + (right-left)//2
            y = (len(n1)+len(n2)+1)//2 - x
            xl = n1[x-1] if x!=0 else float('-inf')
            xr = n1[x] if x!=len(n1) else float('inf')
            yl = n2[y-1] if y!=0 else float('-inf')
            yr = n2[y] if y!=len(n2) else float('inf')
            if xl<=yr and yl<=xr:
                if (len(n1)+len(n2))%2==0:
                    return (max(xl,yl)+min(xr,yr))/2.0
                else:
                    return max(xl, yl)
            elif xl>yr:
                right = x-1
            else:
                left = x+1
        return -1            
