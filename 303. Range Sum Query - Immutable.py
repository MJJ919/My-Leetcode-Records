'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int i, int j) Return the sum of the elements of the nums array in the range [i, j] inclusive (i.e., sum(nums[i], nums[i + 1], ... , nums[j]))
'''
Method below is brute force, kinda awkward.
'''

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.data = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        sum = 0
        for a in range(i,j+1):
            sum = sum + self.data[a]
        return sum
  
'''
Method below uses caching.
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
