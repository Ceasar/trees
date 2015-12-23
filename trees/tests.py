from .autovivify import AutovivifiedDict
from .objectify import ObjectifiedDict
from .heap import heap


def test_objectified_getattr():
    d = {'foo': 1, 'bar': 2}
    od = ObjectifiedDict(d)
    assert od.foo == 1
    assert len(od) == 2


def test_objectified_getitem():
    d = {'foo': 1, 'bar': 2}
    od = ObjectifiedDict(d)
    assert od['foo'] == 1
    assert len(od) == 2


def test_objectified_missing():
    d = {'foo': 1, 'bar': 2}

    class LazyD(ObjectifiedDict):
        def __missing__(self, key):
            return 0

    ld = LazyD(d)
    assert ld['foobar'] == 0
    assert len(ld) == 3


def test_objectify_setattr():
    d = {'foo': 1, 'bar': 2}
    od = ObjectifiedDict(d)
    od.foobar = 0
    assert od['foobar'] == 0
    assert len(od) == 3


def test_objectify_setitem():
    d = {'foo': 1, 'bar': 2}
    od = ObjectifiedDict(d)
    od['foobar'] = 0
    assert od['foobar'] == 0
    assert len(od) == 3


def test_autovivifed():
    d = AutovivifiedDict()
    d[1][2] = 2
    assert d[1][2] == 2


def test_autovivifed2():
    d = AutovivifiedDict()
    d[1][2] = 2
    d[1][3] = 3
    assert d[1][3] == 3


def heap_factory():
    h = heap()
    h.push(1)
    h.push(3)
    h.push(2)
    return h


def test_heap():
    h = heap_factory()
    assert h.top == 1
    assert h.pop() == 1
    assert h.top == 2
    assert h.pop() == 2


def test_heap_empty():
    h = heap_factory()
    assert h.pop() == 1
    assert h.pop() == 2
    assert h.pop() == 3
    assert h.empty


def test_heap_contains():
    h = heap_factory()
    assert h.pop() == 1
    assert 1 not in h
    assert 2 in h
    assert 3 in h
    assert h.pop() == 2
    assert 2 not in h
    assert 3 in h
