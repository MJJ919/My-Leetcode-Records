'''
https://leetcode.com/problems/split-array-largest-sum/
Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.
Write an algorithm to minimize the largest sum among these m subarrays.

Example 1:
Input: nums = [7,2,5,10,8], m = 2
Output: 18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
'''
'''
Time:O(nlgn)
Space:O(1)
'''
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        big = sum(nums)
        small = max(nums)
        def check(n):
            count=1
            cursum=0
            for num in nums:
                cursum += num
                if cursum>n:
                    count+=1
                    cursum = num
                    if count>m: return False
            return True
            
        while big>=small:
            mid = small + (big-small)//2
            if check(mid):
                big = mid-1
            else:
                small = mid+1
        return small
