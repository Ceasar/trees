"""
Object wrapper for dictionaries. Replaces item notation with attribute
notations. (a['foo'] -> a.foo)

Note, the wrapper obscures all standard dictionary methods.

For historical purposes it is worth noting that there is no effective way to
include standard dictionary methods nor maintain internal dictionaries since
there is no clean way to set any attributes on the object. At best, we might
make future improvements by fully inverting the attribute notation of dicts
with the item notation, thus allowing things like "x['keys']" to replace
dict.keys.

Heavily inspired by: http://stackoverflow.com/a/6573827/577199
"""
from collections import Container, Sized, Iterable
import six


class ObjectifiedDict(Container, Sized, Iterable):
    """Wrapper for a dict to give it an object interface.

    Does not include access to any dict instance methods.

    >>> d = {'foo': 1, 'bar': {'a': 3, 'b': 4}}
    >>> OD = type('OD', (ObjectifiedDict,), {'__missing__': lambda s, k: 0})
    >>> o = OD(d)
    >>> o # doctest: +SKIP
    {'foo': 1, 'bar': {'a': 3, 'b': 4}}
    >>> o.foo
    1
    >>> o["foo"]
    1
    >>> o.bar.a
    3
    >>> o.foobar
    0
    >>> o.barfoo = 1
    >>> o.barfoo
    1
    """
    def __init__(self, mapping=None, **kwargs):
        if mapping:
            for k, v in six.iteritems(mapping):
                self[k] = v
        for k, v in kwargs:
            self[k] = v

    def __setattr__(self, k, v):
        self[k] = v

    def __setitem__(self, k, v):
        """Update the object with new data."""
        new_value = v
        if isinstance(v, dict):
            new_value = type(self)(v)
        elif isinstance(v, list):
            new_value = [(type(self)(e) if isinstance(e, dict) else e)
                         for e in v]
        self.__dict__[k] = new_value

    def __getattr__(self, key):
        """Get an attribute."""
        return self[key]

    def __missing__(self, key):
        raise KeyError(key)

    def __getitem__(self, key):
        if key in self.__dict__:
            return self.__dict__[key]
        else:
            # If __missing__ is defined, cache the result
            self[key] = val = self.__missing__(key)
            return val

    def __contains__(self, key):
        return key in self.__dict__

    def __len__(self):
        return len(self.__dict__)

    def __iter__(self):
        return iter(self.__dict__)

    def __repr__(self):
        return repr(self.__dict__)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
