from collections import Container, Sized, Iterable


class Resource(Container, Sized, Iterable):
    """Wrapper for a dict to give it an object interface.

    Does not permit of any dict instance methods.

    >>> d = {'foo': 1, 'bar': {'a': 3, 'b': 4}}
    >>> MyResource = type('MyResource', (Resource,), {'_load': lambda: 0})
    >>> o = MyResource(d)
    >>> o
    {'foo' : 1, 'bar' : {'a' : 3, 'b' : 4}}
    >>> o.foo
    1
    >>> o["foo"]
    1
    >>> o.bar.a
    3

    Heavily inspired by: http://stackoverflow.com/a/6573827/577199
    """
    def __init__(self, mapping=None, **kwargs):
        if mapping:
            for k, v in mapping.iteritems():
                self[k] = v
        for k, v in kwargs:
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
        """Get a missing attribute."""
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
