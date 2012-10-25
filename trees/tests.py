from autovivify import AutovivifiedDict
from objectify import ObjectifiedDict


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
