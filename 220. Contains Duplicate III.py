'''
Given an array of integers, find out whether there are two distinct indices i and j in the array 
such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
'''
'''
Time:O(nlgn)
Space:O(n)
'''
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        nums = sorted([(i,nums[i]) for i in range(len(nums))], key=lambda y : y[1])
        i,j = 0, 0 
        while i < len(nums):
            while j < i and nums[i][1] - nums[j][1] > t:
                j+=1
            for l in range(j,i):
                if abs(nums[l][0] - nums[i][0]) <= k:
                    return True
            i+=1        
            
        return False
