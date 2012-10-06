import nose

from autovivify import AutovivifiedDict


def test_autovivifed():
    d = AutovivifiedDict()
    d[1][2] = 2
    assert d[1][2] == 2


def test_autovivifed2():
    d = AutovivifiedDict()
    d[1][2] = 2
    d[1][3] = 3
    assert d[1][3] == 3
