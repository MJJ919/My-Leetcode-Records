'''
https://leetcode.com/problems/maximum-number-of-removable-characters/
You are given two strings s and p where p is a subsequence of s. 
You are also given a distinct 0-indexed integer array removable containing a subset of indices of s (s is also 0-indexed).

You want to choose an integer k (0 <= k <= removable.length) such that, 
after removing k characters from s using the first k indices in removable, 
p is still a subsequence of s. More formally, you will mark the character at s[removable[i]] for each 0 <= i < k, 
then remove all marked characters and check if p is still a subsequence.

Return the maximum k you can choose such that p is still a subsequence of s after the removals.
A subsequence of a string is a new string generated from the original string with some characters 
(can be none) deleted without changing the relative order of the remaining characters.

Example 1:
Input: s = "abcacb", p = "ab", removable = [3,1,0]
Output: 2
Explanation: After removing the characters at indices 3 and 1, "abcacb" becomes "accb".
"ab" is a subsequence of "accb".
If we remove the characters at indices 3, 1, and 0, "abcacb" becomes "ccb", and "ab" is no longer a subsequence.
Hence, the maximum k is 2.
'''
'''
Time:O(nlgn)
Space:O(n)
'''
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def check(pos):
            remove = set(removable[:pos+1])
            i, j = 0, 0
            while i<len(s) and j<len(p):
                if p[j]==s[i] and i not in remove:
                    j += 1
                i += 1
            return j==len(p)
        
        left = 0
        right = len(removable)
        while left<right:
            mid = left + (right-left)//2
            if check(mid):
                left = mid+1
            else:
                right = mid
        return left
