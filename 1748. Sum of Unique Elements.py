'''
https://leetcode.com/problems/sum-of-unique-elements/
You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.
Return the sum of all the unique elements of nums. 

Example 1:
Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.
'''
'''
Time:O(n)
Space:O(n)
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = Counter(nums)
        res = 0
        for num, fre in counter.items():
            if fre == 1:
                res += num
        return res
