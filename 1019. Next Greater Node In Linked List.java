/*
https://leetcode.com/problems/next-greater-node-in-linked-list/
We are given a linked list with head as the first node.  
Let's number the nodes in the list: node_1, node_2, node_3, ... etc.

Each node may have a next larger value: for node_i, next_larger(node_i) is the node_j.val 
such that j > i, node_j.val > node_i.val, and j is the smallest possible choice.  
If such a j does not exist, the next larger value is 0.

Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).
Note that in the example inputs (not outputs) below, arrays such as [2,1,5] 
represent the serialization of a linked list with a head node value of 2, 
second node value of 1, and third node value of 5.

Example 1:
Input: [2,1,5]
Output: [5,5,0]
*/
/*
Time:O(n)
Space:O(n)
*/
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int[] nextLargerNodes(ListNode head) {
        List<Integer> l = new ArrayList<>();
        Stack<Integer> s = new Stack<>();
        for (ListNode cur = head; cur!=null; cur = cur.next)    l.add(cur.val);
        int n = l.size();
        int[] res = new int[n];
        for (int i=n-1; i>=0; i--){
            int num = l.get(i);
            while (!s.isEmpty() && s.peek()<=num)   s.pop();
            res[i] = s.isEmpty()? 0:s.peek();
            s.add(num);
        }
        return res;
    }
}
