'''
https://leetcode.com/problems/rearrange-string-k-distance-apart/
Given a non-empty string s and an integer k, rearrange the string such that the same characters are at least distance k from each other.
All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".

Example 1:
Input: s = "aabbcc", k = 3
Output: "abcabc" 
Explanation: The same letters are at least distance 3 from each other.
'''
'''
Time:O(nlgn)
Space:O(1)
'''
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k==0:    return s
        counter = Counter(s)
        a = [[-counter[c],c] for c in counter]
        heapq.heapify(a)
        seen = deque()
        res = ''
        
        while len(a) or len(seen):
            if len(seen)==k:
                current = seen.popleft()
                if current[0]<0:
                    heapq.heappush(a, current)
            if len(a):
                current = heapq.heappop(a)
                res += current[1]
                seen.append([current[0]+1, current[1]])
            else:
                if len(res)==len(s):    return res
                else:   return ""
