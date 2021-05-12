/*
https://leetcode.com/problems/target-sum/
You are given an integer array nums and an integer target.
You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

Example 1:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
*/
/*
Time: O(mn)
Space:O(n)
*/
class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        int sum = IntStream.of(nums).sum();
        if (target>sum || target<-sum)  return 0;
        int[] dp = new int[sum*2+1];
        dp[sum+nums[0]] = 1;
        dp[sum-nums[0]] += 1;
        for (int i=1; i<nums.length; i++){
            int[] next = new int[sum*2+1];
            for (int j=-sum; j<=sum; j++){
                if (dp[j+sum]!=0){
                    int n = nums[i];
                    next[j + sum + n] += dp[j + sum];
                    next[j + sum - n] += dp[j + sum];
                }
            }
            dp = next;
        }
        return dp[target+sum];
    }
}

/*
Time:O(mn)
Space:O(mn)
*/
class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        int sum = IntStream.of(nums).sum();
        if (target>sum || target<-sum)  return 0;
        int[][] dp = new int[nums.length][sum*2+1];
        dp[0][sum+nums[0]] = 1;
        dp[0][sum-nums[0]] += 1;
        for (int i=1; i<nums.length; i++){
            for (int j=-sum; j<=sum; j++){
                if (dp[i-1][j+sum]!=0){
                    int n = nums[i];
                    dp[i][j + sum + n] += dp[i-1][j + sum];
                    dp[i][j + sum - n] += dp[i-1][j + sum];
                }
            }
        }
        return dp[nums.length-1][target+sum];
    }
}
