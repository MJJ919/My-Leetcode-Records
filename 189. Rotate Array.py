'''
https://leetcode.com/problems/rotate-array/
Given an array, rotate the array to the right by k steps, where k is non-negative.
Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
 
Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
'''

'''
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a = len(nums)
        nums[:k],nums[k:]=nums[a-k:],nums[:a-k]

'''
Time:O(n)
Space:O(n)
'''
class Solution(object):
    def rotate(self, nums, k):
        """
        n = len(nums)
        a = [0]*n
        for i in range(n):
            a[(i+k)%n] = nums[i]
        nums [:] = a
     
'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        def inverse(nums,i,j):
            while i<j:
                nums[i],nums[j]=nums[j],nums[i]
                i,j=i+1,j-1
        inverse(nums,0,n-1)
        inverse(nums,0,k-1)
        inverse(nums,k,n-1)
