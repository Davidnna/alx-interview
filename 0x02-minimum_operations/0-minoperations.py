#!/usr/bin/python3
"""Defines minOperations"""


def minOperations(n):
    """Performs minOperations on n and
    returns the total number of performed operations to achieve n"""
    if n < 2:
        return 0

    _times = 0
    _max = 2

    while n > 1:
        if not n % _max:
            n //= _max
            _times += _max

        else:
            if _max == 2:
                _max += 1
            else:
                _max += 2

    return _times
