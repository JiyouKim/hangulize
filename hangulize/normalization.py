# -*- coding: utf-8 -*-
"""
    hangulize.normalization
    ~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2010-2016 by Heungsub Lee
    :license: BSD, see LICENSE for more details.
"""
from __future__ import unicode_literals

import unicodedata

from six import viewkeys, viewvalues


__all__ = ['normalize_roman']


def normalize_roman(string, additional=None):
    """Removes diacritics from the string and converts to lowercase::

        >>> normalize_roman(u'Eèé')
        u'eee'

    """
    if additional:
        safe = list(viewkeys(additional)) + list(viewvalues(additional))
        def gen():
            for c in string:
                if c not in safe:
                    yield normalize_roman(c)
                elif c in additional:
                    yield additional[c]
                else:
                    yield c
        return ''.join(gen())
    chars = []
    for c in string:
        if unicodedata.category(c) == 'Lo':
            chars.append(c)
        else:
            nor = unicodedata.normalize('NFD', c)
            chars.extend(x for x in nor if unicodedata.category(x) != 'Mn')
    return ''.join(chars).lower()
