/*
https://leetcode.com/problems/partition-equal-subset-sum/
Given a non-empty array nums containing only positive integers, 
find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
*/
/*
Time:O(n*m)
Space:O(n)
*/
class Solution {
    public boolean canPartition(int[] nums) {
        int sum = IntStream.of(nums).sum();
        int subsum = sum/2;
        if (sum%2 != 0)  return false;
        boolean[] dp = new boolean[subsum+1];
        dp[0] = true;
        for (int num:nums){
            for (int j=subsum; j>=num; j--)
                dp[j] = dp[j]|dp[j-num];
        }
        return dp[subsum];
    }
}

/*
Time:O(n*m)
Space:O(n*m)
*/class Solution {
    public boolean canPartition(int[] nums) {
        int sum = IntStream.of(nums).sum();
        int subsum = sum/2;
        if (sum%2 != 0)  return false;
        boolean[][] dp = new boolean[nums.length+1][subsum+1];
        dp[0][0] = true;
        for (int i=1; i<nums.length+1; i++){
            int cur = nums[i-1];
            for (int j=0; j<subsum+1; j++){
                if (j<cur)  dp[i][j] = dp[i-1][j];
                else    dp[i][j] = (dp[i-1][j] || dp[i-1][j-cur]);
            }
        }
        return dp[nums.length][subsum];
    }
}
