trees
=====

Collection of various tree data structures.

AutovivifiedDict
----------------

An AutovivifiedDict automatically creates new AutovividedDicts if user looks for a missing key. The result is that you can chain together a bunch of keys to store data more easily.

```python
>>> import trees
>>> d = trees.AutovivifiedDict()
>>> d[1][2][3] = 4
>>> d
{1: {2: {3: 4}}
```

heap
----

A [heap](http://en.wikipedia.org/wiki/Heap_(data_structure\)) is a data structure that satisfies the heap property: If A is a parent node of B, then key(A) < key(B). Thus, heaps will always be sorted from smallest to largest.

```python
>> import trees
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
```
