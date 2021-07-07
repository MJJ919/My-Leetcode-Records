'''
https://leetcode.com/problems/top-k-frequent-words/
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. 
If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
'''
'''
Time:O(klgn)
Space:O(n)
'''
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = defaultdict(int)
        for word in words:
            d[word] -= 1
        l = []
        for key, value in d.items():
            heappush(l, (value, key))
        res = []
        for _ in range(k):
            res.append(heappop(l)[1])
        return res
