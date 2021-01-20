'''
https://leetcode.com/problems/maximum-gap/
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
Return 0 if the array contains less than 2 elements.

Example 1:
Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.
'''
'''
Bucket Algorithms.
Time:O(n)
Space:O(b)
'''
class Solution:
    def maximumGap(self, nums: List[int]) -> int:        
        if len(nums) < 2 or min(nums) == max(nums):
            return 0
        a, b = min(nums), max(nums)
        size = math.ceil((b-a)/(len(nums)-1))
        bucket = [[None, None] for _ in range((b-a)//size+1)]
        for n in nums:
            b = bucket[(n-a)//size]
            b[0] = n if b[0] is None else min(b[0], n)
            b[1] = n if b[1] is None else max(b[1], n)
        bucket = [b for b in bucket if b[0] is not None]
        return max(bucket[i][0]-bucket[i-1][1] for i in range(1, len(bucket)))
        
'''
Sort.
Time:O(nlgn)
Space:O(1)
'''
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n<2: return 0
        nums = sorted(nums)
        gap = float('-inf')
        for i in range(1,n):
            gap = max(gap, nums[i]-nums[i-1])
        return gap
