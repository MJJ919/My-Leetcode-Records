'''
https://leetcode.com/problems/repeated-dna-sequences/
All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T', for example: "ACGAATTCCG". 
When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example 1:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:
Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
'''
'''
Time:O((N−L)L)
Space:O((N−L)L)
'''
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res, seen = set(), set()
        for i in range(0, len(s)-9):
            seq = s[i:i+10]
            if seq in seen:
                res.add(seq)
            seen.add(seq)
        return res
