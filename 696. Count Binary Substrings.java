/*
https://leetcode.com/problems/count-binary-substrings/
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, 
and all the 0's and all the 1's in these substrings are grouped consecutively.
Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
*/
/*
Time:O(n)
Space:O(1)
*/
class Solution {
    public int countBinarySubstrings(String s) {
        char flag = s.charAt(0);
        int[] store = new int[s.length()];
        int pre = 0, cur = 1;
        int res = 0;
        for(int i = 1; i<s.length(); i++){
            if (s.charAt(i) == flag)
                cur++;
            else{
                flag = s.charAt(i);
                res += Math.min(pre, cur);
                pre = cur;
                cur = 1;
            }
        }
        res += Math.min(pre, cur);
        return res;
    }
}

/*
Time:O(n)
Space:O(n)
*/
class Solution {
    public int countBinarySubstrings(String s) {
        char flag = s.charAt(0);
        int[] store = new int[s.length()];
        int count = 1;
        int t = 0;
        for(int i = 1; i<s.length(); i++){
            if (s.charAt(i) == flag)
                count++;
            else{
                store[t++] = count; 
                count = 1;
                flag = s.charAt(i);
            }
        }
        store[t] = count;
        int res = 0;
        for (int i = 1; i<=t; i++){
            res += Math.min(store[i-1], store[i]);
        }
        return res;
    }
}
