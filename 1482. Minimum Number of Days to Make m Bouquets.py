'''
https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
Given an integer array bloomDay, an integer m and an integer k.
We need to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.
Return the minimum number of days you need to wait to be able to make m bouquets from the garden. 
If it is impossible to make m bouquets return -1.

Example 1:
Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let's see what happened in the first three days. x means flower bloomed and _ means flower didn't bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.
'''
'''
Time:O(nlgn)
Space:O(1)
'''
class Solution:
    def minDays(self, bloom: List[int], m: int, k: int) -> int:
        if m*k>len(bloom):  return -1
        left = min(bloom)
        right = max(bloom)
        def make(num):
            count = 0
            flower = 0
            for b in bloom:
                if b<=num:
                    flower += 1
                    if flower==k:
                        count += 1
                        flower = 0
                else:
                    flower = 0
            return count
        
        while left<right:
            mid = (left+right)//2
            if make(mid)<m:
                left = mid+1
            else:
                right = mid
        return left
