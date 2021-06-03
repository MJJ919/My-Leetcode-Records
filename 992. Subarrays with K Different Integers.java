/*
https://leetcode.com/problems/subarrays-with-k-different-integers/
Given an array nums of positive integers, call a (contiguous, not necessarily distinct) 
subarray of nums good if the number of different integers in that subarray is exactly k.
(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)
Return the number of good subarrays of nums.

Example 1:
Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
*/
/*
Time:O(n*n)
Space:O(1)
*/
class Solution {
    public int subarraysWithKDistinct(int[] nums, int k) {
        return atMost(nums, k)-atMost(nums, k-1);
    }
    
    private int atMost(int[] nums, int k){
        int res = 0, left = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i=0; i<nums.length; i++){
            int num = nums[i];
            map.put(num, map.getOrDefault(num, 0)+1);
            while (map.size()>k){
                int l = nums[left++];
                map.put(l, map.get(l)-1);
                if (map.get(l)==0)  map.remove(l);
            }
            res += i-left+1;
        }
        return res;
    }
}
