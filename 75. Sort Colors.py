'''
https://leetcode.com/problems/sort-colors/
Given an array nums with n objects colored red, white, or blue, 
sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Follow up:
Could you solve this problem without using the library's sort function?
Could you come up with a one-pass algorithm using only O(1) constant space?

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Example 3:
Input: nums = [0]
Output: [0]
'''
'''
Time:O(N)
Space:O(1)
'''
        cur, i, j = 0, 0, len(nums)-1
        while cur <= j:
            if nums[cur] == 0:
                nums[i], nums[cur] = nums[cur], nums[i]
                i, cur = i+1, cur+1
            elif nums[cur] == 1:
                cur += 1                
            else:
                nums[cur], nums[j] = nums[j], nums[cur]
                j -= 1
