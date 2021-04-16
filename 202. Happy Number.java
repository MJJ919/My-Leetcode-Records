/*
https://leetcode.com/problems/happy-number/
Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, 
replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.
*/
//Time:O(lgn)
//Space:O(lgn)
class Solution {
    private int next(int n){
        int res = 0;
        while (n!=0){
            res += (n%10)*(n%10);
            n = n/10;
        }
        return res;
    }
    public boolean isHappy(int n) {
        Set<Integer> seen = new HashSet<>();
        while(n!=1 && !seen.contains(n)){
            seen.add(n);
            n = next(n);                
        }
        return n==1;
    }
}
        
//Time:O(lgn)
//Space:O(1)
class Solution {
    private int next(int n){
        int res = 0;
        while (n!=0){
            res += (n%10)*(n%10);
            n = n/10;
        }
        return res;
    }
    public boolean isHappy(int n) {
        int slow = n;
        int fast = next(n);
        while (fast!=1 && slow!=fast){
            slow = next(slow);
            fast = next(next(fast));
        }
        return fast==1;
    }
}
