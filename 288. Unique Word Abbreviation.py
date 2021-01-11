'''
https://leetcode.com/problems/unique-word-abbreviation/
The abbreviation of a word is a concatenation of its first letter, the number of characters between the first and last letter, 
and its last letter. If a word has only two characters, then it is an abbreviation of itself.
'''
'''
Time:O(n)
Space:O(n)
'''
class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.d = defaultdict(list)
        for i in dictionary:
            if len(i)<=2:
                self.d[i].append(i)
            else:
                abbr = i[0] + str(len(i)-2) + i[-1]
                self.d[abbr].append(i)
                
    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        w = word[0]+str(len(word)-2)+word[-1]
        if w not in self.d:
            return True
        elif word in self.d[w] and len(self.d[w])==1:
            return True
        else:
            return False
