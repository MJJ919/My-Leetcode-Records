/*
https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.
In one move, you can increment or decrement an element of the array by 1.

Example 1:
Input: nums = [1,2,3]
Output: 2
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
*/
/*
Time:O(nlgn)
Space:O(1)
*/
class Solution {
    public int minMoves2(int[] nums) {
        Arrays.sort(nums);
        int res = 0;
        for (int i=0; i<nums.length; i++)
            res += Math.abs(nums[nums.length/2]-nums[i]);
        return res;
    }
}

class Solution {
    public int minMoves2(int[] nums) {
        Arrays.sort(nums);
        int res = 0;
        int i=0;
        int j=nums.length-1;
        while (i<j) {
            res += nums[j]-nums[i];
            i++;
            j--;
        }
        return res;
    }
}
