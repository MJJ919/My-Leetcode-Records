'''
https://leetcode.com/problems/lru-cache/
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. 
If the number of keys exceeds the capacity from this operation, evict the least recently used key.

Follow up:
Could you do get and put in O(1) time complexity?
Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]
'''
'''
Time:O(1)
Space:O(n)
'''
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.q = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.q:
            self.q.move_to_end(key)
            return self.q[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.q:
            self.q.move_to_end(key)
        self.q[key] = value
        if len(self.q)>self.cap:
            self.q.popitem(last=False)
