/*
https://leetcode.com/problems/factorial-trailing-zeroes/
Given an integer n, return the number of trailing zeroes in n!.
Follow up: Could you write a solution that works in logarithmic time complexity?

Example 1:
Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
*/

/*
Time:O(lgn)
Space:O(1)
*/
class Solution {
    public int trailingZeroes(int n) {
        int count = 0;
        while (n != 0){
            n /= 5;
            count += n;
        }
        return count;
    }
}

/*
Time:O(n)
Space:O(1)
*/
class Solution {
    public int trailingZeroes(int n) {
        int count = 0;
        for(int i=5; i<=n; i+=5){
            int cur = i;
            while (cur%5 == 0){
                count++;
                cur /= 5;
            }
        }
        return count;
    }
}
