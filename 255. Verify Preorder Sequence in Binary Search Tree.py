'''
https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/
Given an array of unique integers preorder, return true if it is the correct preorder traversal sequence of a binary search tree.

Example 1:
Input: preorder = [5,2,1,3,6]
Output: true
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        s = []
        lower = float('-inf')
        for num in preorder:
            if num<lower:
                return False
            while s and num>s[-1]:
                lower = s.pop()
            s.append(num)
        return True
