'''
https://leetcode.com/problems/majority-element-ii/
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
Follow-up: Could you solve the problem in linear time and in O(1) space?

Example 1:
Input: nums = [3,2,3]
Output: [3]

Example 2:
Input: nums = [1]
Output: [1]

Example 3:
Input: nums = [1,2]
Output: [1,2]
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        s1,s2,c1,c2=0,0,None,None
        for i in nums:
            if i == c1:
                s1 += 1
            elif i == c2:
                s2 += 1
            elif s1 == 0:
                c1 = i
                s1 += 1
            elif s2 == 0:
                c2 = i
                s2 += 1
            else:
                s1,s2 = s1-1, s2-1
        result = []
        for i in [c1,c2]:
            if nums.count(i) > len(nums)//3:
                result.append(i)
        return result
