'''
https://leetcode.com/problems/high-five/
Given a list of the scores of different students, items, where items[i] = [IDi, scorei] 
represents one score from a student with IDi, calculate each student's top five average.

Return the answer as an array of pairs result, where result[j] = [IDj, topFiveAveragej] 
represents the student with IDj and their top five average. Sort result by IDj in increasing order.
A student's top five average is calculated by taking the sum of their top five scores and dividing it by 5 using integer division.
'''
'''
Time:O(nlgn)
Space:O(n)
'''
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        for item in items:
            d[item[0]].append(item[1])
        
        res = []
        for idx, mark in d.items():
            avg = sum(i for i in heapq.nlargest(5, mark))//5
            res.append([idx, avg])
        return sorted(res, key = lambda x:x[0])
