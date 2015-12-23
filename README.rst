trees
=====

.. image:: https://badge.fury.io/py/trees.png
    :target: http://badge.fury.io/py/trees

.. image:: https://travis-ci.org/Ceasar/trees.svg
    :target: https://travis-ci.org/Ceasar/trees

Collection of various tree data structures.

Installation
------------

To install trees, simply:

.. code-block:: bash

    $ pip install trees

AutovivifiedDict
----------------

An AutovivifiedDict automatically creates new AutovividedDicts if user looks for a missing key. The result is that you can chain together a bunch of keys to store data more easily.

.. code-block:: python

    >>> import trees
    >>> d = trees.AutovivifiedDict()
    >>> d[1][2][3] = 4
    >>> d
    {1: {2: {3: 4}}

ObjectifiedDict
---------------

An ObjectifiedDict provides a wrapper for dictionaries that allows interaction through object notation. Though not really a tree, an ObjectifiedDict is frequently useful when dealing with trees.

.. code-block:: python

    >>> import trees
    >>> d = {'foo': 1, 'bar': {'red': True}}
    >>> od = trees.ObjectifiedDict(d)
    >>> od
    {'foo': 1, 'bar': {'red': True}}
    >>> od["foo"]
    1
    >>> od.foo
    1
    >>> od.bar.red
    True
    >>> od.car = 1
    >>> od
    {'foo': 1, 'bar': {'red': True}, 'car': 1}
    >>> od.car
    1

heap
----

A heap_ is a data structure that satisfies the heap property: If A is a parent node of B, then key(A) < key(B). Thus, heaps will always be sorted from smallest to largest.

.. code-block:: python

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

.. _heap: http://en.wikipedia.org/wiki/Heap_(data_structure\)
