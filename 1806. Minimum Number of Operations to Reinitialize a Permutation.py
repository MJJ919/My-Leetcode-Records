'''
https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/
You are given an even integer n. You initially have a permutation perm of size n where perm[i] == i (0-indexed).
In one operation, you will create a new array arr, and for each i:

If i % 2 == 0, then arr[i] = perm[i / 2].
If i % 2 == 1, then arr[i] = perm[n / 2 + (i - 1) / 2].
You will then assign arr to perm.

Return the minimum non-zero number of operations you need to perform on perm to return the permutation to its initial value.
'''
'''
Time:O(n)
Space:O(1)
'''
class Solution:
    def reinitializePermutation(self, n: int) -> int:
        s = n//2
        i = s
        count = 1
        while i != 1:
            if i%2 == 0:
                i = i//2
            else:
                i = (i-1)//2 + s
            count += 1
        return count
