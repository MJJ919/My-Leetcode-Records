'''
https://leetcode.com/problems/max-consecutive-ones-iii/
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
'''
'''
Time:O(n*n)
Space:O(1)
'''
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0 
        left = 0
        for idx, num in enumerate(nums):
            if num==0:
                k -= 1
            if k<0:
                while left<=idx and k<0:
                    if nums[left]==0:
                        k += 1
                    left += 1
            res = max(idx-left+1, res)
        return res
        
'''
Time:O(n)
Space:O(n)
'''class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        p1 = 0
        count = 0
        pos = deque()
        for idx, num in enumerate(nums):
            if num==0:
                count += 1 
                pos.append(idx)
            if len(pos)>k:
                p1 = pos.popleft()+1
            res = max(res, idx-p1+1)
        return res
