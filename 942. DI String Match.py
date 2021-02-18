'''
https://leetcode.com/problems/di-string-match/
Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]

Example 1:

Input: "IDID"
Output: [0,4,1,3,2]
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        res = []
        i, j = 0, len(S)
        for ch in S:
            if ch=='I':
                res.append(i)
                i += 1
            else:
                res.append(j)
                j -= 1
        return res+[i]
