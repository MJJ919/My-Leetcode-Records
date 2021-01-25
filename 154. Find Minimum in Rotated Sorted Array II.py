'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.
The array may contain duplicates.

Example 1:
Input: [1,3,5]
Output: 1
'''
'''
Time:O(lgn)
Space:O(1)
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums)-1
        while i<j:
            mid = (i+j)//2
            if nums[mid]<nums[j]:
                j = mid
            elif nums[mid]>nums[j]:
                i = mid+1
            else:
                j -= 1
        return nums[j]
