'''
https://leetcode.com/problems/largest-number/
Given a list of non-negative integers nums, arrange them such that they form the largest number.
Note: The result may be very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"

Example 3:
Input: nums = [1]
Output: "1"

Example 4:
Input: nums = [10]
Output: "10"
'''
class Solution {
    public class compare implements Comparator<String>{
        public int compare(String a, String b){
            String order1 = a+b;
            String order2 = b+a;
            return order2.compareTo(order1);
        }
    }
    public String largestNumber(int[] nums) {
        String[] strnums = new String[nums.length];
        for(int i=0; i<nums.length; i++){
            strnums[i] = String.valueOf(nums[i]);
        }
        Arrays.sort(strnums, new compare());
        if (strnums[0].equals("0"))  return "0";
        String res = new String();
        for (String num: strnums){
            res += num;
        }
        return res;
    }
}  
    
'''
Time:O(nlgn)
Space:O(n)
'''
import functools
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def comparator(n1, n2):
            if int(n1+n2)>int(n2+n1):
                return -1
            else:
                return 1
        nums = [str(x) for x in nums]
        nums.sort(key = functools.cmp_to_key(comparator))
        return ''.join(nums) if nums[0]!= '0' else '0'
