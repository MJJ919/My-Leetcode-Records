'''
https://leetcode.com/problems/group-anagrams/
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
'''
'''
Method below uses defaultdict.
Time:O(NKlogK)
Space:O(NK)
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            ch = ''.join(sorted(i))
            d[ch].append(i)
        return [i for i in d.values()]

'''
Time:O(NK)
Space:O(NK)
'''
class Solution(object):
    def groupAnagrams(self, strs):
        d = defaultdict(list)
        for i in strs:
            count = [0]*26
            for c in i:
                count[ord(c)-ord('a')] += 1
            d[tuple(count)].append(i)
        return d.values()
