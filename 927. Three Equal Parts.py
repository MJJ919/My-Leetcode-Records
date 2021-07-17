'''
https://leetcode.com/problems/three-equal-parts/
You are given an array arr which consists of only zeros and ones, divide the array into 
three non-empty parts such that all of these parts represent the same binary value.

If it is possible, return any [i, j] with i + 1 < j, such that:

arr[0], arr[1], ..., arr[i] is the first part,
arr[i + 1], arr[i + 2], ..., arr[j - 1] is the second part, and
arr[j], arr[j + 1], ..., arr[arr.length - 1] is the third part.
All three parts have equal binary values.
If it is not possible, return [-1, -1].

Note that the entire part is used when considering what binary value it represents. 
For example, [1,1,0] represents 6 in decimal, not 3. Also, leading zeros are allowed, so [0,1,1] and [1,1] represent the same value.

Example 1:
Input: arr = [1,0,1,0,1]
Output: [0,3]
'''
'''
Time:O(n)
Space:O(n)
'''
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        total = sum(arr)
        if total==0:
            return [0, len(arr)-1]
        if total%3 != 0:
            return [-1, -1]
        part = total//3
        res = []
        pos = []
        count = 0
        for idx, num in enumerate(arr):
            if num==1:
                count += 1
                if count in (1, part+1, 2*part+1):
                    pos.append(idx)
                if count in (part, 2*part, 3*part):
                    pos.append(idx)
        if arr[pos[0]:pos[1]]!=arr[pos[2]:pos[3]] or arr[pos[2]:pos[3]]!=arr[pos[4]:pos[5]] or arr[pos[0]:pos[1]]!=arr[pos[4]:pos[5]]:
            return [-1, -1]
        gap1 = pos[2]-pos[1]-1
        gap2 = pos[4]-pos[3]-1
        gap3 = len(arr)-1-pos[5]
        
        if gap3>gap2 or gap3>gap1:
            return [-1, -1]
        pos[1] += gap3
        pos[3] += gap3
        
        return [pos[1], pos[3]+1]
