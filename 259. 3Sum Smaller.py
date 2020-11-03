'''
Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 
0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Follow up: Could you solve it in O(n2) runtime?

Example 1:
Input: nums = [-2,0,1,3], target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
[-2,0,1]
[-2,0,3]

Example 2:
Input: nums = [], target = 0
Output: 0

Example 3:
Input: nums = [0], target = 0
Output: 0
'''

'''
Method below uses 2 pointers.
Time:O(n**2)
Space:O(1)
'''
class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sum = 0
        if len(nums)<3:
            return sum
        nums = sorted(nums)
        for i, ch in enumerate(nums):
            a,b = i+1, len(nums)-1
            while a<b:
                if ch+nums[a]+nums[b]<target:
                    sum = sum+(b-a)
                    a = a+1
                else:
                    b = b-1
        return sum
