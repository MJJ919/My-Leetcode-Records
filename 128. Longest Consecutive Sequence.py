'''
https://leetcode.com/problems/longest-consecutive-sequence/
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
Follow up: Could you implement the O(n) solution? 

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        long = 0
        numset = set(nums)
        
        for num in nums:
            if num-1 not in numset:
                curnum = num
                curlong = 1
                
                while curnum+1 in numset:
                    curnum += 1
                    curlong += 1
                long = max(long, curlong)
        return long
        
'''
Time:O(nlgn)
Space:O(1)
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:    return 0
        nums.sort()
        long = 1
        cur = 1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                if nums[i] == nums[i-1]+1:
                    cur += 1
                else:
                    long = max(long,cur)
                    cur = 1
        return max(cur,long)
