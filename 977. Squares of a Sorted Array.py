'''
https://leetcode.com/problems/squares-of-a-sorted-array/
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
'''
'''
Time:O(nlgn)
Space:O(n)
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([i*i for i in nums])
   
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        res = [0 for _ in range(len(nums))]
        for i in range(len(nums)-1, -1, -1):
            if abs(nums[left])>abs(nums[right]):
                res[i] = nums[left]*nums[left]
                left += 1
            else:
                res[i] = nums[right]*nums[right]
                right -= 1
        return res
