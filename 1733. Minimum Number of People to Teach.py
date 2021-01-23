'''
https://leetcode.com/problems/minimum-number-of-people-to-teach/
'''
'''
Time:O(n**2)
Space:O(n)
'''
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        languages = [set(l) for l in languages]
        cant = set()
        
        for i,j in friendships:
            i,j = i-1, j-1
            if languages[i]&languages[j]:continue
            cant.add(i)
            cant.add(j)
            
        lan = Counter()
        for i in cant:
            for j in languages[i]:
                lan[j] += 1
        return 0 if not cant else len(cant)-max(lan.values())
