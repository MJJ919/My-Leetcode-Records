'''
https://leetcode.com/problems/insert-delete-getrandom-o1/
Implement the RandomizedSet class:
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). 
Each element must have the same probability of being returned.
'''
'''
Use hashmap and list.
Time:O(1)
Space:O(n)
'''
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.l = []
        
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.d:   return False
        self.d[val] = len(self.l)
        self.l.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.d:
            return False
        last, validx = self.l[-1], self.d[val]
        self.l[validx] = last
        self.d[last] = validx
        self.l.pop()
        del self.d[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.l)

'''
Use set.
Time:O(n)
Space:O(n)
'''
class RandomizedSet:

    def __init__(self):
        self.s = set()
    
    def hasval(self, val):
        if val not in self.s:
            return True
        else:   return False

    def insert(self, val: int) -> bool:
        noshow = self.hasval(val)
        if noshow:
            self.s.add(val)
        return noshow
            

    def remove(self, val: int) -> bool:
        noshow = self.hasval(val)
        if not noshow:
            self.s.remove(val)
        return not noshow

    def getRandom(self) -> int:
        return random.choice(list(self.s))
