'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
'''

'''
Method below uses defaultdict.
Time:O(NKlogK)
Space:O(NK)
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = collections.defaultdict(list)
        for i in strs:
            dict[tuple(sorted(i))].append(i)
        return dict.values()
