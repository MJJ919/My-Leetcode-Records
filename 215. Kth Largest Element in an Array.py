'''
https://leetcode.com/problems/kth-largest-element-in-an-array/
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

'''
'''
Time:O(n) for average. O(n*n) for the worst.
Space:O(1)
'''
'''
class Solution {
    public int findKthLargest(int[] nums, int k) {
        divide(nums, 0, nums.length-1, k);
        return nums[nums.length-k];
    }
    
    private void divide(int[] nums, int i, int j, int k){
        if (j<i)    return;
        int pos = conquer(nums, i, j);
        if (pos == nums.length-k)   return;
        else if (pos > nums.length-k)  divide(nums, i, pos-1, k);
        else    divide(nums, pos+1, j, k);
    }
    
    private int conquer(int[] nums, int i, int j){
        int wall = i;
        int mark = nums[j];
        for (int pos=i; pos<j; pos++){
            if (nums[pos]<mark) swap(nums, pos, wall++);
        }
        swap(nums, wall, j);
        return wall;
    }
    
    private void swap(int[] nums, int i, int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
'''

'''
Time:O(nlgk)
Space:O(k)
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
