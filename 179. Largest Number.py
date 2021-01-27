'''
https://leetcode.com/problems/largest-number/
Given a list of non-negative integers nums, arrange them such that they form the largest number.
Note: The result may be very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"

Example 3:
Input: nums = [1]
Output: "1"

Example 4:
Input: nums = [10]
Output: "10"
'''
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def mergesort(nums, i, j):
            if i>j:
                return 
            if i == j:
                return [nums[i]]
            mid = (i+j)//2
            left = mergesort(nums, i, mid)
            right = mergesort(nums, mid+1, j)
            return merge(left, right)
            
        def merge(l1, l2):
            res = []
            i, j = 0, 0
            while i<len(l1) and j<len(l2):
                if str(l1[i])+str(l2[j])>str(l2[j])+str(l1[i]):
                    res.append(l1[i])
                    i += 1
                else:
                    res.append(l2[j])
                    j += 1
            res += l1[i:] or l2[j:]
            return res
            
        nums = mergesort(nums, 0, len(nums)-1)
        return str(int(''.join(str(i) for i in nums)))        
    
'''
Time:O(nlgn)
Space:O(n)
'''
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = map(str, nums)
        nums.sort(cmp = lambda x, y: cmp(x + y, y + x), reverse = True)
        return '0' if nums[0] == '0' else ''.join(nums)
