"""
Implementation of an auto-vivified dict.
"""


class AutovivifiedDict(dict):
    '''
    Implementation of an auto-vivified dict.

    Auto-vivified objects will automatically create a new object of type(self)
    when a user queries for a missing key.

    Based on: http://stackoverflow.com/a/6781411/577199

    >>> d = AutovivifiedDict()
    >>> d[1][2][3] = 4
    >>> d
    {1: {2: {3: 4}}}
    '''
    def __missing__(self, key):
        # If a user tries to access a missing key, create a new object
        # of type(self) and set the key to that.
        value = self[key] = type(self)()
        return value


if __name__ == "__main__":
    import doctest
    doctest.testmod()
