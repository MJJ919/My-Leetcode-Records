/*
https://leetcode.com/problems/count-number-of-nice-subarrays/
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
Return the number of nice sub-arrays.

Example 1:
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
*/
/*
Time:O(n*n)
Space:I(1)
*/
class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        return atMost(nums, k)-atMost(nums, k-1);
    }
    public int atMost(int[] nums, int k){
        int res = 0;
        int count = 0;
        int left = 0;
        for (int i=0; i<nums.length; i++){
            if (nums[i]%2==1)   count++;
            while (count>k){
                if (nums[left++]%2==1)  count--;
            }
            res += i-left+1;
        }
        return res;   
    }
}
