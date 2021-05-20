/*
https://leetcode.com/problems/longest-increasing-subsequence/
Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. 
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
*/
/*
Time:O(n**2)
Space:O(n)
*/
class Solution {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        if (n==0) return 0;
        int[] dp = new int[n];
        dp[0] = 1;
        int res = 1;
        for (int i=1; i<n; i++){
            int cur = 0;
            for (int j=0; j<i; j++){
                if (nums[j]<nums[i]){
                    cur = Math.max(cur, dp[j]);
                }
            }
            dp[i] = cur+1;
            res = Math.max(dp[i], res);
        }
        return res;
    }
}
       
/*
Time:O(nlgn)
Space:O(n)
*/
class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] dp = new int[nums.length];
        int len = 0;
        for (int num:nums){
            int i = Arrays.binarySearch(dp, 0, len, num);
            if (i<0)    i = -(i+1);
            dp[i] = num;
            if (i==len) len++;
        }
        return len;
    }
}
