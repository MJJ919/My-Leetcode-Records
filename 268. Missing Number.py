'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
'''

'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        bit = 0
        for i in range(n+1):
            bit ^= i
        for num in nums:
            bit ^= num
        return bit
            
'''
Time:O(n)
Space:O(1)
'''
class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        return (n*(n+1)/2-sum(nums))
