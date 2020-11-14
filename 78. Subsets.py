'''
Given an integer array nums, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. 

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
'''

'''
Method below uses cascading.
Time:O(n*2^n)
Space:O(n*2^n)
'''
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output=[[]]
        for i in nums:
            output = output+[cur + [i] for cur in output]
        return output

'''
method below uses bitmap.
Time:O(n*2^n)
Space:O(n*2^n)
'''
class Solution(object):
    def subsets(self, nums):
        output = []
        n = len(nums)
        for i in range(2**n,2**(n+1)):
            bit = bin(i)[3:]
            output.append([nums[j] for j in range(n) if bit[j]=='1'])
        return output
