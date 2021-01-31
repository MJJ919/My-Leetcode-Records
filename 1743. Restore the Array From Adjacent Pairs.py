'''
https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/
'''
class Solution:
    def restoreArray(self, pairs: List[List[int]]) -> List[int]:
        def dfs(u):
            res.append(u)
            visited[u] = True
            for edge in d[u]:
                if visited[edge] == False:
                    dfs(edge)
            
        d = defaultdict(list)
        for pair in pairs:
            d[pair[0]].append(pair[1])
            d[pair[1]].append(pair[0])
        edge = [i for i in d if len(d[i])==1]
        res = []
        visited = {i:False for i in d}
        dfs(edge[0])
        return res
