'''
https://leetcode.com/problems/group-shifted-strings/249. Group Shifted Strings
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:
"abc" -> "bcd" -> ... -> "xyz"
Given a list of non-empty strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:
Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
'''
'''
Time:O(n**2)
Space:O(n)
'''
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strings:
            ch = str()
            for j in range(len(i)-1):
                diff = (26+ord(i[j])-ord(i[j-1]))%26
                ch += str(diff)
            d[ch].append(i)
        return d.values()
