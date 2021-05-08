/*
https://leetcode.com/problems/put-boxes-into-the-warehouse-i/
You are given two arrays of positive integers, boxes and warehouse, 
representing the heights of some boxes of unit width and the heights of n rooms in a warehouse respectively. 
The warehouse's rooms are labelled from 0 to n - 1 from left to right where warehouse[i] (0-indexed) is the height of the ith room.

Example 1:
Input: boxes = [4,3,4,1], warehouse = [5,3,3,4,1]
Output: 3
*/
/*
Time:O(nlgn)
Space:O(1)
*/
class Solution {
    public int maxBoxesInWarehouse(int[] b, int[] w) {
        int m = b.length;
        int n = w.length;
        int count = 0;
        Arrays.sort(b);
        for (int i=m-1; i>=0; i--){
            if (b[i]<=w[count]) {
                count++;
            }
            if (count == n)    break;
        }
        return count;
    }
}

/*
Time:O(nlgn)
Space:O(1)
*/
class Solution {
    public int maxBoxesInWarehouse(int[] b, int[] w) {
        for (int i=1; i<w.length; i++){
            w[i] = Math.min(w[i-1], w[i]);
        }
        Arrays.sort(b);
        int count = 0;
        for (int i=w.length-1; i>=0; i--){
            int room = w[i];
            if (count<b.length && room>=b[count]) count += 1;
        }
        return count;
    }
}
