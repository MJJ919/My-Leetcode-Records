'''
https://leetcode.com/problems/next-permutation/
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
The replacement must be in place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """            
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        def reverse(a):
            i, j = a, len(nums)-1
            while i<j:
                swap(i, j)
                i, j = i+1, j-1
                
        i = len(nums)-2
        while i>=0 and nums[i+1]<=nums[i]:
            i -= 1
        j = len(nums)-1
        if i>=0:
            while j>i and nums[j]<=nums[i]:
                j -= 1
            swap(i, j)
        reverse(i+1)
