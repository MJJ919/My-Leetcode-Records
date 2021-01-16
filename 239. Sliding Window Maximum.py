'''
https://leetcode.com/problems/sliding-window-maximum/
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n*k==0:  return []
        if k==1:    return nums
        left, right = [0]*n, [0]*n
        left[0], right[n-1] = nums[0], nums[n-1]
        for i in range(1,n):
            if i%k==0:   
                left[i] = nums[i]
            else:   
                left[i] = max(left[i-1], nums[i])
            j = n-i-1
            if (j+1)%k==0:  
                right[j] = nums[j]
            else:
                right[j] = max(right[j+1], nums[j])
        res = []
        for i in range(n-k+1):
            res.append(max(left[i+k-1], right[i]))
        return res
