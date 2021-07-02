'''
https://leetcode.com/problems/rearrange-words-in-a-sentence/
Given a sentence text (A sentence is a string of space-separated words) in the following format:
First letter is in upper case.
Each word in text are separated by a single space.
Your task is to rearrange the words in text such that all words are rearranged in an increasing order of their lengths.
If two words have the same length, arrange them in their original order.

Return the new text following the format shown above.

Example 1:
Input: text = "Leetcode is cool"
Output: "Is cool leetcode"
Explanation: There are 3 words, "Leetcode" of length 8, "is" of length 2 and "cool" of length 4.
Output is ordered by length and the new first word starts with capital letter.
'''
'''
Time:O(nlgn)
Space:O(n)
'''
class Solution:
    def arrangeWords(self, text: str) -> str:
        d = defaultdict(list)
        for word in text.split(' '):
            d[len(word)].append(word)
        res = ''
        for l, word in sorted(d.items()):
            for w in word:
                if not res:
                    res += w[0].upper()+w[1:]
                else:
                    res += ' '
                    res += w.lower()
        return res
