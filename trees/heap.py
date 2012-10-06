"""
Convenience wrapper for the functional heapq library.
"""
import heapq


# TODO: add a __contains__ method
class heap(object):
    '''A tree-based data structure that satisfies the heap property.

    A heap can be used as priority queue by pushing tuples onto the heap.

    >>> import trees
    >>> h = trees.heap()
    >>> h.push(1)
    >>> h.push(3)
    >>> h.push(2)
    >>> h.top
    1
    >>> h.pop()
    1
    >>> h.top
    2
    >>> h.pop()
    2
    >>> h.pop()
    3
    >>> h.empty
    True
    '''
    def __init__(self, items=None):
        if items is None:
            items = []
        self._items = list(items)
        heapq.heapify(self._items)

    @property
    def top(self):
        return self._items[0]

    @property
    def empty(self):
        return len(self) == 0

    def pop(self):
        '''Pop and return the smallest item from the heap, maintaining the heap
        invariant. If the heap is empty, IndexError is raised.
        '''
        try:
            return heapq.heappop(self._items)
        except IndexError as e:
            raise e

    def push(self, item):
        '''Push the value item onto the heap, maintaining the heap invariant.
        If the item is not hashable, a TypeError is raised.
        '''
        try:
            hash(item)
        except TypeError as e:
            raise e
        else:
            heapq.heappush(self._items, item)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        while len(self) > 0:
            yield self.pop()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
