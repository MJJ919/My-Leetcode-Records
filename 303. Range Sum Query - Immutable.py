'''
https://leetcode.com/problems/range-sum-query-immutable/
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
Implement the NumArray class:
NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int i, int j) Return the sum of the elements of the nums array in the range [i, j] inclusive (i.e., sum(nums[i], nums[i + 1], ... , nums[j]))
'''
'''
Time:O(n)
Space:O(n)
'''

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sum = [] 
        a = 0
        for i in nums:
            a = a + i
            self.sum.append(a)
            
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i>0:
            return (self.sum[j]-self.sum[i-1])
        else:
            return self.sum[j]    
