'''
https://leetcode.com/problems/search-insert-position/
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
'''
'''
Time:O(logn)
Space:O(1)
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)-1
        while i<=j:
            mid = (i+j)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                i += 1
            else:
                j -= 1
        return i
