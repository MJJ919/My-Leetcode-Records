/*
https://leetcode.com/problems/sum-of-two-integers/
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:
Input: a = 1, b = 2
Output: 3
*/
/*
Bit munipulation.
Time:O(1)
Space:O(1)
*/
class Solution {
    public int getSum(int a, int b) {
        while (b!=0){
            int carry = a&b;
            a ^= b;
            b = carry<<1;
        }
        return a;
    }
}
