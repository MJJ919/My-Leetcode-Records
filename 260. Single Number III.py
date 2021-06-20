'''
https://leetcode.com/problems/single-number-iii/
Given an integer array nums, in which exactly two elements appear only once and
all the other elements appear exactly twice. 
Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

Example 1:
Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        bitmask = xor&(-xor)
        num1 = 0
        num2 = 0
        for num in nums:
            if num&bitmask:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]
