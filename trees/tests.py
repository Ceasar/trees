from autovivify import AutovivifiedDict
from objectify import ObjectifiedDict


def test_objectified():
    d = {'foo': 1, 'bar': 2}

    class LazyD(ObjectifiedDict):
        def __missing__(self, key):
            return 0

    ld = LazyD(d)
    assert ld['foo'] == 1
    assert ld['bar'] == 2
    assert len(ld) == 2

def test_objectified_expands():

    d = {'foo': 1, 'bar': 2}

    class LazyD(ObjectifiedDict):
        def __missing__(self, key):
            return 0

    ld = LazyD(d)
    assert ld['foobar'] == 0
    assert len(ld) == 3


def test_autovivifed():
    d = AutovivifiedDict()
    d[1][2] = 2
    assert d[1][2] == 2


def test_autovivifed2():
    d = AutovivifiedDict()
    d[1][2] = 2
    d[1][3] = 3
    assert d[1][3] == 3
