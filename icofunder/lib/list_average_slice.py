#!/usr/bin/env python
# -*- coding: utf-8 -*-


def _gen(list_data, number):
    l = [i for i in range(len(list_data))]
    return [l[i:i + number] for i in range(0, len(l), number)]


def gen(list_data, number):
    b = []
    c = _gen(list_data, number)
    for i in c:
        b.insert(c.index(i), [])
        for j in i:
            b[c.index(i)].append(list_data[j])

    return b
