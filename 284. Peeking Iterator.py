'''
https://leetcode.com/problems/peeking-iterator/
Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- 
it essentially peek() at the element that will be returned by the next call to next().

Example:
Assume that the iterator is initialized to the beginning of the list: [1,2,3].
Call next() gets you 1, the first element in the list.
Now you call peek() and it returns 2, the next element. Calling next() after that still return 2. 
You call next() the final time and it returns 3, the last element. 
Calling hasNext() after that should return false.
'''
'''
Time:O(1)
Space:O(1)
'''
class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self._next = iterator.next()
        self._iterator = iterator
        
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self._next

    def next(self):
        """
        :rtype: int
        """
        if self._next is None:   raise StopIteration()
        num  = self._next
        self._next = None
        if self._iterator.hasNext():
            self._next = self._iterator.next()
        return num
    
    def hasNext(self):
        """
        :rtype: bool
        """
        return self._next is not None
