'''
https://leetcode.com/problems/sort-an-array/
Given an array of integers nums, sort the array in ascending order.

Example 1:
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
'''
'''
Time:
Space:
'''
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(nums, left, right):
            if left>=right:
                return 
            pivot = nums[right]
            i = left-1
            for j in range(left, right):
                if nums[j]<=pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i+1], nums[right] = nums[right], nums[i+1]
            quicksort(nums, left, i)
            quicksort(nums, i+1, right)
            
        quicksort(nums, 0, len(nums)-1)
        return nums
