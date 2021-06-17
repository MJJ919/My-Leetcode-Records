'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).
Each node will have a reference to its parent node. The definition for Node is below:
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T 
is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        a = p
        b = q
        while a!=b:
            a = a.parent if a else q
            b = b.parent if b else p
        return a
        
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        s = set()
        while p:
            s.add(p)
            p = p.parent
        while q not in s:
            q = q.parent
        return q
