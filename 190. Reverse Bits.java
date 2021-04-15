/*
https://leetcode.com/problems/reverse-bits/

Example 1:
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, 
so return 964176192 which its binary representation is 00111001011110000010100101000000
*/
/*
Time:O(1)
Space:O(1)
*/
public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int res = 0;
        for(int power=31; power>=0; power--){
            res += (n&1)<<power;
            n = n>>1;
        }
        return res;
    }
}
