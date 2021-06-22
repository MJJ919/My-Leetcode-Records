'''
https://leetcode.com/problems/alien-dictionary/
There is a new alien language that uses the English alphabet. 
However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, 
where the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in 
lexicographically increasing order by the new language's rules. If there is no solution, return "". 
If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, 
the letter in s comes before the letter in t in the alien language. 
If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.

Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
'''
'''
Time:
Space:
'''
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        d = defaultdict(set)
        l = defaultdict(int)
        q = deque()
        valid = True
        count = 0
        res = []
        
        for word in words:
            for ch in word:
                l[ch] = 0
                
        def compare(w1, w2):
            nonlocal valid
            if len(w1)>len(w2) and w1.startswith(w2):
                valid = False
                print(valid)
            for i in range(min(len(w1), len(w2))):
                ch1 = w1[i]
                ch2 = w2[i]
                if ch1!=ch2:
                    if ch2 in d[ch1]:
                        return 
                    else:
                        d[ch1].add(ch2)
                        l[ch2] += 1
                        break
                
        for i in range(len(words)-1):
            compare(words[i], words[i+1])
            
        if not valid:
            return ''
        
        for ch in l:
            if l[ch] == 0:
                res.append(ch)
                q.append(ch)
        while q:
            n = q.popleft()
            for ch in d[n]:
                l[ch] -= 1
                if l[ch]==0:
                    q.append(ch)
                    res.append(ch)
        
        return ''.join(res) if len(res)==len(l) else ''
